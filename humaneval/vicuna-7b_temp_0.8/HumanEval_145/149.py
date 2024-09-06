
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
    if not nums:
        return []

    digit_sums = {digit: nums.count(digit) for digit in '0123456789'}
    sorted_nums = sorted(digit_sums.items(), key=lambda x: x[1], reverse=True)

    index_map = {}
    for i, (digit, count) in enumerate(sorted_nums):
        index_map[digit] = i
    reverse_map = {i: digit for i, digit in index_map.items()}

    return [num for i, num in enumerate(nums) if i in reverse_map]
