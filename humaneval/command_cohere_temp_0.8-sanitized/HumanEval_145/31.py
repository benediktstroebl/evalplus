def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorteed list based on criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which digit sum is calculated.

    Returns:
        int: Sum of the digits of the given number.
    """
    sum_so_far = 0
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        sum_so_far += digit
        temp_num //= 10
    return sum_so_far
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number whose index is sought.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums else 0