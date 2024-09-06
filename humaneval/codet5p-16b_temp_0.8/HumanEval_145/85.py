
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

    from collections import defaultdict

    d = defaultdict(list)

    for i in nums:
        s = 0
        for j in str(i):
            s += int(j)
        d[s].append(i)
    
    return d[sorted(d.keys())[0]]

