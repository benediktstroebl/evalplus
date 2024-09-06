
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
    """
    For each number in the list, find the sum of its digits and store it in a list.
    Sort the list of sums and get the corresponding indices from the original list.
    Return the original list in the order of the indices.
    """
    return nums[list(map(int, nums)).index]

