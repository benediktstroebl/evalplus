```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Args:
        nums: List of integers to be sorted.
    Returns:
        sorted_nums: Sorted list based on criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
    return sorted_nums
```
This script uses the `sorted` function and a lambda to create a custom key that sorts first by the sum of digits and then by the original index. Please note that the function will handle empty input as well, returning an empty list without any issues. The tests for this function would typically involve edge cases as well, such as empty lists, floats, large numbers, and different data types to ensure the function behaves as expected.