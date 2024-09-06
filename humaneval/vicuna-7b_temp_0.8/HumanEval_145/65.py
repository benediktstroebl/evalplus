
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
    # Using two pointers p1 and p2 to iterate through the list
    # p1 is pointed to the first non-negative integer
    # p2 is pointed to the first negative integer
    p1, p2 = 0, 0
    while p1 < len(nums):
        if nums[p1] >= 0:
            p1 += 1
        elif nums[p1] < 0:
            p2 += 1
        else:
            # Adding 1 to p1 since the sum of the digits of -n is n
            p1 += 1
            p2 += 1
    return nums[p1:p2+1]
