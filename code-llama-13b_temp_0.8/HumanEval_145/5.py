
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

    # create list of tuples where the 1st item is the element,
    # and the 2nd item is the sum of its digits
    # [(1, 1), (11, 2), (-1, 1), (-11, 2), (-12, 3)]
    tuples = list(map(lambda e: (e, sum(map(int, str(e)))), nums))

    # sort by 2nd item in tuple (sum of digits)
    return list(map(lambda e: e[0], sorted(tuples, key=lambda e: (e[1], e[0]))))

