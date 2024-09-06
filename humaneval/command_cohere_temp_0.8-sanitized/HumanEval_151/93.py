def double_the_difference(nums):
    odd_squares = sum(num**2 for num in nums if num % 2 and num >= 0 and isinstance(num, int))
    return int(odd_squares)