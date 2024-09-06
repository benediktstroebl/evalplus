
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
    # Transform list of integers to list of tuples,
    # where the tuple is a pair of the number and the sum of its digits
    tuples = [(num, sum(int(c) for c in str(num))) for num in nums]
    # Sort tuples based on the sum of digits
    tuples.sort(key=lambda t: t[1])
    # Get the original list of integers using their indexes
    return [nums[i] for _, i in tuples]


