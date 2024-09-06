
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
    # 文件中的代码
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

    # 我的代码
    # def order_by_points(nums):
    #     x = sorted(nums)
    #     y = [sum(map(int,str(x))) for x in nums]
    #     y.sort()
    #     return [x for x, y in zip(nums, y)]

    # def order_by_points(nums):
    #     x = sorted(nums)
    #     y = [sum(map(int,str(x))) for x in nums]
    #     z = [x for x,y in zip(nums,y)]
    #     return z
