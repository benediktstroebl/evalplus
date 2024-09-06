```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum (non-stable sorting)
    sorted_idx = sorted(range(len(nums)), key=lambda i: (digit_sums[i], i))

    # Reconstruct the sorted list by the original index
    return [nums[i] for i in sorted_idx]
```

This approach uses a combination of sorting and integer conversion to achieve the desired behavior. The key innovation is sorting by a tuple of the digit sum and the original index as a tiebreaker. It sorts using the sum of digits as the primary criterion and the original index as a secondary criterion. The sort is ensured to be stable, meaning the original order of equal elements is preserved.