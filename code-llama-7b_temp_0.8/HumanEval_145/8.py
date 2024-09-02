
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

    # calculate sum of digits in list
    def sum_digits(num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num = num // 10
        return digit_sum

    # sort list according to sum of digits
    nums = sorted(nums, key=sum_digits)

    # sort list according to index
    def index(num):
        return nums.index(num)

    nums = sorted(nums, key=index)

    return nums

