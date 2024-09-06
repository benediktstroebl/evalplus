def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums, ignoring negative or non-integer numbers."
    result = 0
    for num in nums:
        if isinstance(num, int) and num % 2:
            result += num ** 2
    return result