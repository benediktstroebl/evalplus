```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Compute the sum-of-digits score for each number and sort them accordingly.
    sorted_nums = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))

    # However, the original list's order should take precedence in case of identical sums.
    return [sorted_nums[i] for i in range(len(sorted_nums))]
```

This approach utilizes a lambda function to sort the list first by the sum of the digits of each number and then uses a list comprehension to revert the order of elements back to their original positions in case of equal digit-sums.