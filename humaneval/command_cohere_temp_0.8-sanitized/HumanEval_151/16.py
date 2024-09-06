def double_the_difference(nums):
    odd_and_positive = [x for x in nums if x > 0 and isinstance(x, int) and x % 2 != 0]
    return sum(x * x for x in odd_and_positive)