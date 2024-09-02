
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
    # pass
    dct = {}
    l = []
    for n in nums:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1

    for k, v in dct.items():
        l.append((k, v))
    l.sort(key=lambda x: (sum(map(int, str(x[0]))), -x[1]))
    return [i[0] for i in l]

