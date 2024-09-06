
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

    def get_sum(num):
        sum = 0
        for i in range(len(str(num))):
            sum += int(str(num)[i])
        return sum

    nums.sort(key=get_sum)
    return nums

