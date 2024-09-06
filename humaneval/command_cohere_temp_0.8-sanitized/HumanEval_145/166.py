def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria.
    """
    if len(nums) == 0:
        return []
    sorted_ = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number whose digit-sum needs to be calculated.

    Returns:
        int: Sum of the digits of the given number.
    """
    sum_ = sum(map(int, str(num)))
    return sum_
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    index_ = nums.index(num)
    return index_