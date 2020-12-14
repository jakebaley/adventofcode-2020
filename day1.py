def part1(nums):
    for i in nums:
        for j in nums:
            if i + j == 2020:
                return i * j


with open('inputs/day1.txt') as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]
    print(part1(inputs))
    print('Done')
