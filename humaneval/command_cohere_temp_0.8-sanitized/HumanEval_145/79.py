def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # Ensure the list is not empty
    if not nums:
        return []

    # Use a sorting algorithm that handles ties between list items efficiently
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))

    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.
    """
    return sum(int(d) for d in str(num))
def x_index(num):
    """
    Return the index of the given number in the original list.
    """
    return nums.index(num) if nums else 0
nums = [1, 11, -1, -11, -12]