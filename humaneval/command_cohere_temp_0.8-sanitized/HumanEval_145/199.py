def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_so_far = 0
    num_string = str(num)
    for digit in num_string:
        sum_so_far += int(digit)
    return sum_so_far
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we determine the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums else 0