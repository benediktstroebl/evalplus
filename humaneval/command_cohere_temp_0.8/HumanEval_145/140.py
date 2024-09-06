```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the digit in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list according to criteria above
    """
    if not nums:
        return []

    # Keep track of digit sums and original indices for sorting ties.
    digit_sum_indices = []
    for idx, num in enumerate(nums):
        digits = [int(d) for d in str(num)]
        digit_sum = sum(digits)
        digit_sum_indices.append((digit_sum, idx))

    # Sort by sum of digits with tiebreaker.
    return [num for digit_sum, idx in sorted(digit_sum_indices)]
```

The function `order_by_points` sorts a list of integers according to the sum of the digits in each number with the tiebreaker being the index of the number in the original list. It will return the ordered list as required.