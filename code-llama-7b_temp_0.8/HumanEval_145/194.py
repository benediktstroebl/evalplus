
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
    # order_by_points = lambda x: [int(y) for y in str(sum([int(z) for z in str(x)]))]
    result = []
    for i in nums:
        result.append([sum([int(c) for c in str(i)]), i])
    result = sorted(result)
    return [r[1] for r in result]

