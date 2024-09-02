
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
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deem it longer)
    nums.sort(key=lambda n: sum(digits(abs(n))))
    # END_YOUR_CODE
    return nums

