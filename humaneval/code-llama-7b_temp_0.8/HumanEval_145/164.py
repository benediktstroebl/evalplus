
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
    for i in nums:
        points = 0
        num = abs(i)
        while num != 0:
            points += num % 10
            num = num // 10
        result.append((points, i))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return [i[1] for i in result]

