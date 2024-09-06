
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
    # Order all items by their sum of digits.
    # For example, 10 = 1 + 0 and 212 = 2 + 1 + 2.
    items = sorted(enumerate(nums), key=lambda pair: sum(int(i) for i in str(pair[1])))
    # Reverse the list to get the order from lowest to highest value.
    return [i for _, i in reversed(items)]

