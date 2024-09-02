
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
    # binary function to compute sum of digits
    def sum_of_digits(n):
        while n > 0:
            n //= 10
        return n

    # helper function to compute position of a number in original list
    def index(n):
        return nums.index(n)

    # main sorting function
    def sort_by_points(nums):
        sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), index(x)))
        return [x[0] for x in sorted_nums]

    return sort_by_points(nums)