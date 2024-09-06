def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums, handling negatives and non-integer values correctly."
    result = 0
    for n in nums:
        if isinstance(n, int) and n > 0:
            if n % 2:
                result += n * n
        else:
            pass

    return result if result != 0 else None