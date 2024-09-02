
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
    a = []
    for i in range(len(nums)):
        a.append((nums[i],i))
    a.sort(key=lambda x: sum(map(int,str(x[0]))))
    b = []
    for i in range(len(a)):
        b.append(a[i][0])
    return b
