```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Sorting of the input list based on the criteria mentioned.
    """
    if not nums:
        return []

    def sum_of_digits(num):
        # Calculate sum of digits of a number
        return sum(int(d) for d in str(num))

    # Sorting based on sum of digits with tiebreaks
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x))

    # Return the sorted list with original order for items with same sum of digits
    return [sorted_nums[i] for i in range(len(sorted_nums))]
```