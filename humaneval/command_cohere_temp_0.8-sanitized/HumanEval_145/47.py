def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Returns:
        List: Sorting order of given integers based on sum of digits and index.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given integer.

    Example:
        >>> sum_of_digits(12) == 10
        True

    Returns:
        int: Sum of the digits of the given integer.
    """
    sum = 0
    temp = num
    while temp > 0:
        sum += temp % 10
        temp //= 10
    return sum