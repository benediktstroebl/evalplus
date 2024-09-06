def double_the_difference(nums):
    odd_squares = [x**2 for x in nums if x % 2 != 0 and x >= 0]
    return sum(odd_squares) if odd_squares else 0