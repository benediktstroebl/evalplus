def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums."
    result = sum(x**2 for x in nums if x % 2 and x > 0 and isinstance(x, int))
    return result