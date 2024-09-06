def double_the_difference(nums):
    "Sum of squares of odd integers, ignoring negative or non-integer numbers."
    result = 0
    for num in nums:
        if num % 2 and isinstance(num, int) and num >= 0:
            result += num ** 2
    return result