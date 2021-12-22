# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Count the number of sonar measurements that are larger than the one preceding
# DEPRECATED by default sonar_sweep_window
def sonar_sweep(input):
    total_larger = 0
    report = open(input, 'r')
    depths = report.readlines()
    for i in range(1, len(depths)):
        if int(depths[i]) > int(depths[i-1]):
            total_larger += 1
    report.close()
    return total_larger

# Sweep window across the measurements, summing, and return the number of windows that are larger than
# the preceding. Alternative solution: since window step size is 1, could just compare the first number
# of the preceding window with the last number of the current (compare i and i - window_size)
def sonar_sweep_window(input, window_size=1):
    total_larger = 0
    report = open(input, 'r')
    depths = [int(line) for line in report.readlines()]
    # transform depths list into sliding window sums list
    windows = [sum(depths[i-window_size:i]) for i in range(window_size, len(depths) + 1)]
    for i in range(1, len(windows)):
        if windows[i] > windows[i-1]:
            total_larger += 1
    report.close()
    return total_larger


# Test sonar sweep with the sample sonar measurements at https://adventofcode.com/2021/day/1
def test_sonar_sweep():
    test_input_file = 'testinput.txt'
    actual_window1 = sonar_sweep_window(test_input_file)
    actual_window3 = sonar_sweep_window(test_input_file, 3)
    # Part 1 test
    if actual_window1 == 7:
        print("Test Passed")
    else:
        print("Test Failed: Expected 7, Actually", actual_window1)
    # Part 2 test
    if actual_window3 == 5:
        print("Test Passed")
    else:
        print("Test Failed: Expected 5, Actually", actual_window3)



if __name__ == '__main__':
    #test_sonar_sweep()
    print("Part 1:", sonar_sweep_window('input.txt'))
    print("Part 2:", sonar_sweep_window('input.txt', 3))


