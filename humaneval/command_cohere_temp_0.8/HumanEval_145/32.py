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

    # Calculate the sum-of-digits score for each number
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Tiebreaker: sort by original index if digit sums are equal
    sorted_nums = sorted(zip(nums, digit_sums), key=lambda x: [x[1], x[0][0]])

    # Extract the sorted numbers and remove the digit sums (since we're done with them)
    return [n for n, _ in sorted_nums]
```

This approach utilizes a combination of sorting and indexing to achieve the desired outcome. Essentially, we first sum the digits of each number in the list to obtain a `digit_sums` array. Then, we use sorting algorithms to organize the list based on these digit sums, with the tiebreaker being the original index of each number in the list. This logic ensures that numbers with equal digit sums are sorted by their index. Finally, we extract the sorted list of numbers, which now fulfills the specified criteria.