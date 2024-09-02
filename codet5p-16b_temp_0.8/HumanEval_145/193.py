
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
    if len(nums) <= 1:
        return nums
    else:
        for i in range(len(nums)):
            res.append(i)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a = sum(map(int, list(str(nums[i]))))
                b = sum(map(int, list(str(nums[j]))))
                if a < b:
                    res[i], res[j] = res[j], res[i]
    return [nums[i] for i in res]
    
