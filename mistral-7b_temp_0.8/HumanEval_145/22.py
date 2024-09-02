
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

    new_list = []
    # 将所有数字的数字求和
    for number in nums:
        number_sum = sum(map(int, str(number)))
        new_list.append((number, number_sum))
    # 按照数字和排序，然后按照数字的初始位置排序
    new_list.sort(key=lambda x: (x[1], x[0]))
    # 排序后列表切片获取初始列表中的值
    return [x[0] for x in new_list]
