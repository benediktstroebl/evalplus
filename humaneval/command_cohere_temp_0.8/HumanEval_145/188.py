```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on index.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_indices = sorted(range(len(nums)), key=lambda i: (digit_sums[i], i))

    # Reconstruct the sorted list based on the sorted indices.
    sorted_nums = [nums[i] for i in sorted_indices]
    return sorted_nums
```

This function takes a list of integers (`nums`) as input and sorts them according to the sum of their digits, with tiebreakers based on the index of the integers in the original list. The function first calculates the sum of digits for each number in the list using a list comprehension and stores these values in the `digit_sums` list. It then sorts the indices of the numbers accordingly using the `sorted` function with a custom key function that sorts by the digit sum and the original index as a secondary key. Finally, it reconstructs the sorted list from these sorted indices and returns the result.