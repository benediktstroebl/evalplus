
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

    res = []
    for n in nums:
        sum_digits = 0
        for c in str(abs(n)):
            sum_digits += int(c)
        res.append((sum_digits, -n))

    res.sort()
    result = [abs(n) for s, n in res]
    return result

