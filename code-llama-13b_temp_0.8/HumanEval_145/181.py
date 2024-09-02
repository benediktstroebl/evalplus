
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
    # task: sort by key, if key is the same, keep initial order
    # use itemgetter to get key and keep order
    # python3: use key=sum_of_digits, reverse=True
    return sorted(nums, key=lambda item: (sum_of_digits(item), item))
    # return sorted(nums, key=lambda item: (sum_of_digits(item), item), reverse=True)

