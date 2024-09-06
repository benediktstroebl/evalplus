```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum (using Python's default sorting, which is ascending)
    sorted_indices = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Reconstruct the sorted list based on the sorted indices
    sorted_list = [nums[i] for i in sorted_indices]

    return sorted_list
```

This approach uses a combination of numerical sorting and list indexing to achieve the desired ordering. The `sorted_indices` list is first generated, sorting it with the key function applying the digit sum of each index. Then, the original list is reconstructed using these sorted indices to achieve the desired order.