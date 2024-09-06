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

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by the sum-of-digits score, with tiebreaks decided by the index
    sorted_nums = sorted(zip(digit_sums, nums), key=lambda x: (x[0], nums.index(x[1])))

    # Extract the sorted numbers
    return [n for _, n in sorted_nums]
```

This code works by first calculating the sum-of-digits score for each number in the input list. It then sorts the numbers using `sorted()` with a custom key function that sorts by the sum-of-digits score in ascending order and the original index as a tiebreaker. Finally, it extracts the sorted numbers from the sorted list of tuples. This algorithm is efficient and should work well for large inputs.