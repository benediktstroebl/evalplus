
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
    # sort the list in descending order according to the sum of their digits
    sorted_nums = sorted(nums, key=lambda x: sum(int(d) for d in str(x)))

    # if there is more than one item with the same sum of digits,
    # return the items in their original order
    if len(sorted_nums) > 1:
        return sorted_nums
    else:
        return [x for x in sorted_nums]