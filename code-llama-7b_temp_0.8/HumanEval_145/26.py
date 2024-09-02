
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
    # X1
    # return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x))
    # X2
    # return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), str(nums.index(x))))
    # X3
    # return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x))[::-1]
    # X4
    # return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x), reverse=True)
