```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on indices.

    Args:
        nums (list): List of integers

    Returns:
        list: Sorting based on sums of digits and indices.
    """
    if not nums:
        return []

    # Iterate through the list and calculate the sum of digits for each integer
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]

    # Sort the list based on the sum of digits (and indices if ties)
    sorted_nums = sorted(range(len(nums)), key=lambda i: [digit_sums[i], i])

    # Convert the sorted indices back to the original list elements
    return [nums[idx] for idx in sorted_nums]
```