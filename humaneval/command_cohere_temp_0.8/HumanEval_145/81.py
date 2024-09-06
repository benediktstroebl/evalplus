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

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]
    sorted_idx = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Reconstruct the sorted list based on the original indices.
    return [nums[idx] for idx in sorted_idx]
```

This approach leverages Python's `str.join` together with `sorted` to achieve the desired sorting. Specifically, the code turns each number into its individual digits using a generator expression, sums these digits, and then employs `sorted` in combination with a custom key function to sort based on the digit sums. Finally, the sorted list is reconstituted using the original indices. 

Note that this solution adheres to Python styling conventions with the addition of comments to enhance readability and maintainability. Let me know if you'd like to further refine the code or if you have any more questions!