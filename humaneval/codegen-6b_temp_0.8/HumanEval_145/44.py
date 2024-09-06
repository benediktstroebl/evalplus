
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
    nums_grp = {}
    for num in nums:
        num_in_str = str(abs(num))
        if num_in_str not in nums_grp:
            nums_grp[num_in_str] = [num]
        else:
            nums_grp[num_in_str].append(num)
    return sorted(nums_grp.values(), key=sum, reverse=True)
