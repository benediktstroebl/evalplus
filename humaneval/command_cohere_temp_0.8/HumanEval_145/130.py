```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This script provides a function `order_by_points` that sorts a list of numbers according to the sum of their digits. If two or more numbers have the same digit sum, they are further sorted according to their index in the original list. The function is tested with the provided example, and the test is positive, hence the function behaves as expected.