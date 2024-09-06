
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
    # convert input list to a set to remove duplicates
    nums_set = set(nums)
    # sort the set in descending order based on the sum of the digits
    sorted_nums_set = sorted(nums_set, key=lambda x: sum(map(int, x)))
    # convert the sorted set back to a list and return it
    return sorted_nums_set
