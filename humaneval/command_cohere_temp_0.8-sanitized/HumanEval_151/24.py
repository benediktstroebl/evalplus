def double_the_difference(nums):
    "Sum of squares of odd integers in list"
    result = 0
    for x in nums:
        if isinstance(x, int) and x % 2:
            result += x ** 2
    return result if result else 0