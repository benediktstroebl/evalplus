
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
    # sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)
    # add each number to the sum of its digits
    nums_digits = [sum(int(n) for n in d) for d in sorted_nums]
    # add the number to the list of numbers with the same sum of digits
    nums_digits_set = set(nums_digits)
    # add the numbers to the list in their order
    return [d for d in nums_digits_set if d not in [0] + nums_digits_set]
