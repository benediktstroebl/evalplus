
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


    # def digit_sum(n):
    #     return sum([int(num) for num in str(n)])

    # nums.sort(key=digit_sum)
    # return nums


    # return [n for n in nums if digit_sum(n)]

    nums = sorted(nums, key=lambda n: (sum(int(i) for i in str(n)), n), reverse=False)
    return nums
