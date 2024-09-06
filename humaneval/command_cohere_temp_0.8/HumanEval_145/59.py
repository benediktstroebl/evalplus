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
    if len(nums) == 0:
        return []

    # Track the indices of the numbers that have been sorted.
    sorted_indices = []

    # Sort the numbers based on the sum of their digits.
    for i in range(len(nums)):
        digit_sum = sum(int(d) for d in str(nums[i]))
        if digit_sum not in sorted_indices:
            sorted_indices.append(digit_sum)
        elif i == len(nums) - 1 or nums[i] != nums[sorted_indices.index(digit_sum)]:
            sorted_indices.append(digit_sum)

    # Restore the original order for numbers with the same digit sum.
    sorted_nums = [nums[idx] for idx in sorted_indices]
    return sorted_nums
```

This approach uses a "tracking index" method, which tracks the indices of the sorted elements within the original list while sorting and then restores the original order for elements with the same digit sum.