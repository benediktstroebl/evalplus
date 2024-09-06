```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```

This script sorts the list of numbers `nums` in ascending order based on the sum of the digits of each number. If two or more numbers have the same digit sum, the original list's index is used as a tiebreaker. The result is returned as a new list `sorted_nums`.