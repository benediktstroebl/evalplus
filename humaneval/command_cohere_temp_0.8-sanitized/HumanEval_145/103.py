def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list according to criteria above
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums
def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number
    """
    numstr = str(num)
    return sum(int(digit) for digit in numstr)
def x_index(num):
    """
    Detect the index of the given number in the original list
    """
    return nums.index(num) if nums != [] else -1
nums = [1, 11, -1, -11, -12]