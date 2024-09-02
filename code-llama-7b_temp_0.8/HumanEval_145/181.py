
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
    sum_of_digits = lambda x: sum(int(digit) for digit in str(x))
    indices = [i for i in range(len(nums))]
    indices_of_sum_of_digits = [(i, sum_of_digits(n)) for i, n in enumerate(nums)]
    indices_of_sum_of_digits.sort(key=lambda x: x[1])
    sorted_indices = [idx for idx, _ in indices_of_sum_of_digits]
    return [nums[i] for i in sorted_indices]
