
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
    dict = {}
    for num in nums:
        if sum([int(num) for num in str(num)]) not in dict:
            dict[sum([int(num) for num in str(num)])] = [num]
        else:
            dict[sum([int(num) for num in str(num)])].append(num)
    result = []
    for key in sorted(dict.keys()):
        result += sorted(dict[key])
    return result
