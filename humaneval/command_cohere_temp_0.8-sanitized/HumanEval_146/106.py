def specialFilter(nums):
    odd_digits = [int(digit) for digit in nums if int(digit) % 2 == 1]
    return sum(num for num in nums if len(odd_digits) == 2 and num > 10)