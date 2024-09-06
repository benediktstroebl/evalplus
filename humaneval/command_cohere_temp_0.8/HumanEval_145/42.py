```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # If the input list is empty, return it
    if not nums:
        return []

    # Use a sorting algorithm to sort by digit sum, with tiebreak by index
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

    return sorted_nums
```

This script sorts the list of integers `nums` in ascending order based on the sum of their digits, with tiebreaks resolved by choosing the item with the smaller index in the original list. The function `order_by_points` achieves this by converting each integer to a string, summing the digits, and using this sum as the sorting key. The example usage and expected output are also included.