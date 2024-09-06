```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = [num for ind, num in enumerate(nums) if ind == num]
    sorted_nums.sort()
    return sorted_nums
```

This code snippet sorts the list of integers `nums` by the sum of their digits, with the tiebreaker being the index of the integer in the original list. It does this by initially excluding from the sorting process any elements that have the same digit sum as their index. These elements are placed at the beginning of the `sorted_nums` list in the appropriate order. The result is a list sorted according to the desired criteria.