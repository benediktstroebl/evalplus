
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
    # your code here
    list = nums.copy()
    list_sum = []
    i = 0
    while i < len(list):
        list_sum.append(sum([int(j) for j in str(list[i])]))
        i += 1
    list_sum = list(filter(bool, list_sum))
    result = [list[list_sum.index(j)] for j in list_sum]
    return result
