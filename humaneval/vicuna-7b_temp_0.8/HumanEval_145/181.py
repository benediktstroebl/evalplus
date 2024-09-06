
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
    # Create a new list of digits
    digits = [int(n) for n in str(num)]
    # Sort the digits
    digits.sort()
    # Convert the digits back to integers
    for i, d in enumerate(digits):
        nums[i] = d
    return nums