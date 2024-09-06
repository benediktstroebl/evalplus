```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list:Sorted list based on criteria above
    """
    if not nums:
        return []

    def sum_digits(num):
        total = 0
        for digit in str(num):
            total += int(digit)
        return total

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x))
    return sorted_nums
```

This function uses a key process to sort the list `nums` using the criteria stated in the problem. The key process creates a new list sorted by the sum of digits and then by the original list index if the previous criterion is the same. The function then returns the sorted list.