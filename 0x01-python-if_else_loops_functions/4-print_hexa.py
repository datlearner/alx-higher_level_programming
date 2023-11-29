#!/usr/bin/python3
def myFunction(number):
    nums = '0123456789abcdef'
    t_n = number // 16
    sin_gle = number % 16
    if t_n > 0:
        return nums[t_n] + nums[sin_gle]
    else:
        return nums[sin_gle]


if __name__ == '__main__':
    for number in range(99):
        print('{:d} = 0x{}'.format(number, myFunction(number)))
