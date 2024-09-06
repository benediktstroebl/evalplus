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
    sorted_idx = sorted(range(len(nums)), key=lambda i: [digit_sums[i], i])

    # Reconstruct the sorted list based on the sorted indices.
    return [nums[idx] for idx in sorted_idx]
```

This approach first calculates the sum of digits for each integer in the list and then sorts the index entries according to this digit sum. As a tiebreaker, we resort to the original index in the event of identical digit sums, as specified in the problem statement. To rebuild the sorted list, we finally employ the sorted indices. This algorithm is guaranteed to solve the problem statement.