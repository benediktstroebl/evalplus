
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
    # 下面的sort_by_points函数，根据points计算出的值排序
    def sort_by_points(nums):
        points = [(num, points(num)) for num in nums]
        points.sort(key=lambda x: x[1])
        return [point[0] for point in points]

    # 下面的points函数，计算一个数的点数
    def points(num):
        if not isinstance(num, (int, float)):
            raise TypeError
        if num == 0:
            return 0
        points = 0
        while num > 0:
            points += num % 10
            num = int(num / 10)
        return points

    # 下面的order_by_points函数，在sort_by_points函数的基础上添加处理索引的逻辑
    def order_by_points(nums):
        sorted_nums = sort_by_points(nums)
        for i, num in enumerate(nums):
