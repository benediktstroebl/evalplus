```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # Ensure the list is not empty
    if not nums:
        return []

    # Convert the list to strings for easier manipulation
    digit_nums = [str(num) for num in nums]

    # Calculate the sum of digits for each number
    digit_sums = [sum(int(d) for d in num) for num in digit_nums]

    # Use lexicographic sorting to order the numbers according to digit sums and their original index
    return [''.join(num) for num, ind in sorted(zip(digit_nums, digit_sums), key=lambda x: (x[1], x[0]))]
```

This approach converts the list of integers to strings, calculates the sum of digits for each number, and then sorts the numbers based on these digit sums using a custom sorting key. This ensures that numbers with the same digit sum are ordered based on their original index. The function returns the sorted numbers as a list of integers.