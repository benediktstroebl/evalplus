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
    sorted_digits = sorted(zip(digit_sums, nums), key=lambda x: (x[0], x[1][0]))

    # Extract the sorted numbers and return.
    return [num for digit_sum, num in sorted_digits]
```

This approach creates a list `digit_sums` that represents the digit sum for each number in the input list. It then combines this with the original number using `zip`, and sorts them using a custom key in the `sorted` function, first by the digit sum and then by the original list index as a tiebreaker. Finally, it extracts the sorted numbers and returns the result.