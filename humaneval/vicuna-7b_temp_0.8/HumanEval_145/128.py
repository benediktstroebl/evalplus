
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
    result = []
    for num in nums:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum > 0:
            result.append(num)
        elif num < 0:
            result.append(num)
        else:
            result.append(digit_sum)
    return result
