def double_the_difference(nums):
    odd_and_valid = [num for num in nums if num % 2 != 0 and num >= 0 and isinstance(num, int)]
    return sum(num ** 2 for num in odd_and_valid)