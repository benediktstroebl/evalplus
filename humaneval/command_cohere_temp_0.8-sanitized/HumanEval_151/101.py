def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in nums:
        if num % 2 != 0 and num > 0:
            result += num ** 2
    return result