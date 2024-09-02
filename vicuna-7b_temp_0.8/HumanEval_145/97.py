
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
    # This is not the most efficient way to do this
    # but it should work and is good enough for this problem
    # The idea is to iterate through the list and for each number
    # check if the number is positive or negative and
    # if it is positive or negative, return it in the same order as it is
    # in the list, otherwise, return it in a different order
    return [x for x in nums if x > 0 or x < 0]