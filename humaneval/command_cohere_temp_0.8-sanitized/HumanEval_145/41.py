def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # If the list is empty, return it.
    if not nums:
        return []

    # Use a sorting algorithm that handles ties between list items efficiently.
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))

    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
    - num (int): Number for which we want to calculate the sum of digits.

    Returns:
    - int: Sum of digits of the given number.
    """
    return sum(int(d) for d in str(num))
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
    - num (int): Number for which we want to determine the index.

    Returns:
    - int: Index of the given number in the original list.
   bc
    """
    return nums.index(num)