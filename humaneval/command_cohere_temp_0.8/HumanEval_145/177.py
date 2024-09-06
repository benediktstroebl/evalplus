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

    # Calculate the total digit sum for each number
    digit_sums = [sum(int(d) for d in str(num)) for num in nums]

    # Sort by digit sum (default sorting method)
    sorted_by_digit_sum = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Map the index numbers back to the original list
    sorted_nums = [nums[i] for i in sorted_by_digit_sum]

    return sorted_nums
```

This approach utilizes the `sorted` function and the `key` parameter to sort the list by the sum of digits. After calculating the digit sums, we sort the indices of the original list and use this sorted index to retrieve the corresponding elements from the original list. This ensures that the numbers with higher digit sums come first, and in case of equal digit sums, the original order is preserved as the tiebreaker.