
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
    # find the sum of all digits of each number
    digits_sum = [sum(map(int, str(n))) for n in nums]
    # sort the list
    sorted_nums = sorted(zip(digits_sum, nums), key=lambda x: (x[0], x[1]))
    # sort the sorted list
    return sorted([x[1] for x in sorted_nums])

