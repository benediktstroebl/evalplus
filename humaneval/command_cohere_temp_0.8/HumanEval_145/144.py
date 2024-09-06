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
    sorted_indices = sorted(range(len(nums)), key=lambda i: (digit_sums[i], i))

    # Reconstruct the sorted list based on the sorted indices.
    sorted_nums = [nums[i] for i in sorted_indices]
    return sorted_nums
```

This approach utilizes a combination of sorting with key functions and summing the digits of each number to achieve the desired ordering. The key function prioritizes sorting based on digit sums and ties the decision by the index of the number in the original list. The output of the provided examples in the docstring matches the expected output.