def specialFilter(nums):
    odd_digits = [int(digit) for digit in nums if digit % 2 != 0]
    return sum(num for num in nums if num > 10 and int(num[0]) in odd_digits and int(num[-1]) in odd_digits)