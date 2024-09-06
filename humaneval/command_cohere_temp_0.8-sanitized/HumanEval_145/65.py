def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list according to specified criteria
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number
    """
    return sum(int(d) for d in str(num))
def x_index(num):
    """
    Find the index of the given number in the original list
    """
    return nums.index(num) if nums == list(set(nums)) else -1
nums = [1, 11, -1, -11, -12]