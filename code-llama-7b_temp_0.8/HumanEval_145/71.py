
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
    dct = {}
    for ind, num in enumerate(nums):
        sum_digit = sum([int(x) for x in str(num)])
        if sum_digit in dct:
            dct[sum_digit].append(ind)
        else:
            dct[sum_digit] = [ind]
    result = []
    for key in sorted(dct.keys()):
        result.extend(dct[key])
    return [nums[x] for x in result]

