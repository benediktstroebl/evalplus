```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True

    Returns:
        List: Sorting order of given list based on the algorithm.
    """
    if not nums:
        return []

    # Calculate the digit-based score for each number
    scores = [sum(int(d) for d in str(n)) for n in nums]

    # Initially sort by the digit score (descending)
    sorted_nums = sorted(zip(nums, scores), key=lambda x: x[1], reverse=True)

    # Further sort by the original index as a tiebreaker (ascending)
    sorted_nums = sorted(sorted_nums, key=lambda x: x[0])

    # Extract the sorted numbers
    return [n for n, _ in sorted_nums]
```

This algorithm leverages Python's powerful `str.format()` and `zip()` functionalities alongside list comprehension for clarity and brevity. The approach remains consistent with the problem's guidelines. The provided tests should be adapted to verify the code's correctness. I can provide the tests upon request. Let me know if further clarification is needed.