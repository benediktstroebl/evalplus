```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # List of tuples for sorting: (sum_digits, index_in_original_list)
    sorted_idx = [(ds, i) for i, (ds, n) in enumerate(zip(digit_sums, nums))]

    # Sort by sum of digits with tiebreaker (index)
    sorted_idx.sort(key=lambda x: (x[0], x[1]))

    return [nums[i] for ds, i in sorted_idx]
```

This code calculates the sum of the digits for each number and then creates a list of tuples pairing each sum with its original index. It sorts these tuples using a custom key function that prioritizes the sum of digits followed by the index. Finally, it returns the sorted numbers by indexing back into the original list from the sorted tuples.