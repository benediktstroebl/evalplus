def double_the_difference(nums):
    "Sum of squares of odd integers in list"
    result = 0
    for n in nums:
        if isinstance(n, int) and n % 2:
            result += n ** 2
    return result if result else 0