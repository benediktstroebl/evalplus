
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
    def helper(num, total):
        if num == []:
            return []
        else:
            if num[0] + total[0] == total[1]:
                return helper(num[1:], total[1:]) + [num[0]]
            else:
                return helper(num[1:], total[1:]) + [num[0]]

    return helper(nums, [sum(map(int, str(n))), sorted(nums)])
