
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
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort(key=lambda x: sum(int(digit) for digit in str(x[0])), reverse=True)
    return [num[0] for num in nums_with_index]
