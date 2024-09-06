
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
    # pass
    # assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # assert order_by_points([]) == []

    if not nums:
        return []

    result = []
    list_points = []

    for i in range(len(nums)):
        sum_num = 0
        for ch in str(nums[i]):
            sum_num += int(ch)
        list_points.append((sum_num, nums[i]))

    list_points.sort(key=lambda x: x[0])

    for i in range(len(list_points)):
        result.append(list_points[i][1])

    return result

