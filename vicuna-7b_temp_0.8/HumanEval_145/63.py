
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
    # initialize list of sums of digits
    sums = [0] * len(nums)
    # fill the list of sums of digits
    for i, num in enumerate(nums):
        sums[i] = sum(int(d) for d in str(num))
    # sort the list
    sorted_nums = sorted(nums, key=lambda x: sums[x])
    return [x for x in sorted_nums]
