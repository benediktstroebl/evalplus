def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for n in nums:
        if isinstance(n, int) and n % 2 != 0 and n != 0:
            result += n ** 2
    return result