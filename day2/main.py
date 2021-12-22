import numpy as np


def move_submarine(input):
    # Direction hash map as unit vectors in (x, y), where down is the positive y direction
    DIRECTION = {
        "forward": np.array([1, 0]),
        "down": np.array([0, 1]),
        "up": np.array([0, -1])
    }
    pos = np.array([0, 0])
    report = open(input, 'r')
    moves = [line.split() for line in report.readlines()]
    for move in moves:
        dir = move[0]
        num = int(move[1])
        pos = pos + DIRECTION.get(dir) * num
    return pos


def move_submarine_aim(input):
    # Direction dictionary as unit vectors in (x, y, aim), where down is the positive y direction
    DIRECTION = {
        "forward": np.array([1, 0, 0]),
        "down": np.array([0, 0, 1]),
        "up": np.array([0, 0, -1])
    }
    pos = np.array([0, 0, 0]) # (x, y, aim)
    report = open(input, 'r')
    moves = [line.split() for line in report.readlines()]
    for move in moves:
        dir = move[0]
        num = int(move[1])
        pos = pos + DIRECTION.get(dir) * num
        if dir == "forward":
            pos[1] += pos[2] * num
    return pos[0:2]


# Test sonar sweep with the sample sonar measurements at https://adventofcode.com/2021/day/2
def test_move_submarine():
    test_input_file = 'testinput.txt'
    test_part1 = np.prod(move_submarine(test_input_file))
    test_part2 = np.prod(move_submarine_aim(test_input_file))
    # Part 1 test
    if test_part1 == 150:
        print("Part 1 Test Passed")
    else:
        print("Part 1 Test Failed: Expected 150, Actually", test_part1)
    # Part 2 test
    if test_part2 == 900:
        print("Part 2 Test Passed")
    else:
        print("Part 2 Test Failed: Expected 900, Actually", test_part2)


if __name__ == "__main__":
    #test_move_submarine()
    print("Part 1:", np.prod(move_submarine("input.txt")))
    print("Part 2:", np.prod(move_submarine_aim("input.txt")))
