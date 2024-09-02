
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
    dict1 = {}
    for i in nums:
        sum1 = 0
        for j in str(i):
            sum1 += int(j)
        dict1[sum1] = i

    list1 = list(dict1.values())
    list1.sort(key=nums.index)

    return list1

