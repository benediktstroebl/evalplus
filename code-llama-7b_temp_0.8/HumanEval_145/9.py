
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
    # 4 5 6 7 8 9 2 3 1 0
    # 0 1 2 3 4 5 6 7 8 9

    # reverse_dict = {i: s for s, i in enumerate(sorted(set(sum(map(int, str(n)) for n in nums))))}
    # return sorted(nums, key=lambda n: reverse_dict[sum(map(int, str(n)))])
    reverse_dict = {}
    for n in nums:
        s = sum(map(int, str(n)))
        reverse_dict.setdefault(s, []).append(n)

    return [v[i] for s in sorted(reverse_dict) for i, v in enumerate(reverse_dict[s])]

