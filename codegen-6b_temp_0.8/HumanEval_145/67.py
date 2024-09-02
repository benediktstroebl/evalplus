
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
    dict_nums_to_digit_sum = {}
    for i, num in enumerate(nums):
        num_sum = sum(int(digit) for digit in str(abs(num)))
        dict_nums_to_digit_sum[(num, i)] = num_sum
    return sorted(nums, key=lambda x: (dict_nums_to_digit_sum[(-x, i)], i))

