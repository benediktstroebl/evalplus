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
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort by digit sum (default sorting method)
    sorted_by_digit_sum = sorted(range(len(nums)), key=digit_sums.__getitem__)

    # Map the index numbers back to the original list
    sorted_nums = [nums[i] for i in sorted_by_digit_sum]

    return sorted_nums
```

This algorithm first calculates the total digit sum for each number in the list. It then sorts these numerical indices of the list based on the digit sums using `sorted()`. Finally, it maps the sorted numerical indices back to the original list to obtain the desired sorted result. This algorithm gracefully handles the tiebreaker condition, ensuring reliable sorting. 

This approach boasts a time complexity of O(n log n) due to the inherent efficiency of the built-in sorting algorithm and the numerical sum operation.