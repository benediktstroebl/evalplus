
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Handle base case
    if not nums:
        return []

    # Create a set of unique digits
    digits = {digit for digit in str(nums[0]) + str(nums[1])}

    # Sort the list by the sum of digits and then by index
    sorted_nums = sorted(nums, key=lambda x: (digits.count(str(x)), x))

    return [x for x in sorted_nums if x != 0]
