def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which the digit sum is calculated.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_so_far = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_so_far += digit
        temp //= 10
    return sum_so_far
def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number whose index is to be determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if num in nums else -1