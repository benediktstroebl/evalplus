
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
    # 创建一个空列表来存储已经排序的数字
    sorted_nums = []
    
    # 遍历列表，计算每个数字的点数，并将其加入到列表中
    for num in nums:
        sum_digits = 0
        for digit in str(num):
            sum_digits = sum_digits * 10 + digit - 48
        sorted_nums.append(sum_digits)

    return sorted_nums
