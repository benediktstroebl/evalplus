def double_the_difference(nums):
    "Sum of squares of odd integers, ignoring negatives and non-integers"
    result = 0
    for num in nums:
        if num % 2 != 0 and num > 0:  # Checking for oddness and non-negativity
            result += num * num
    return result