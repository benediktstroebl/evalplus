
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

    nums_sorted_by_index = sorted(nums, key=lambda x: x)
    nums_sorted_by_sum = sorted(nums, key=lambda x: sum(int(y) for y in str(x)))
    # Create a new list of indexes, where each index corresponds to the index of a number in
    # nums_sorted_by_index, which has the same sum of digits as the number at the index of that list.
    # The index of the list corresponds to the index of the number in nums_sorted_by_index.
    indexes = [nums_sorted_by_index.index(num) for num in nums_sorted_by_sum]

    return [nums_sorted_by_index[i] for i in indexes]

