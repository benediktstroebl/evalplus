
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
    res = []

    for num, point in enumerate(nums):
        summ = 0
        for i in str(num):
            summ += int(i)

        res.append((summ, num, point))

    res.sort()
    nums = []
    for point, _, num in res:
        nums.append(num)

    return nums
