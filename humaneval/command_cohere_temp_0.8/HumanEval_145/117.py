```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers
    
    Returns:
        list: Ordered list based on the criteria specified.
    """
    if not nums:
        return []
    summed_nums = [sum(map(int, str(num))) for num in nums]
    sorted_nums = sorted(zip(range(len(nums)), summed_nums), key=lambda x: x[1])
    return [num for i, num in sorted_nums]
```

This code block provides a Python function called `order_by_points` that takes a list of integers as input. This function sorts the list while breaking ties by considering the index of items in the original list. The process involves summing the digits of each number and using these digit sums to sort the numbers. It first creates a list of digit sums for each number, then uses a lambda function as the sorting key to sort the list of integers based on these sums. Finally, it returns the sorted list of integers, fulfilling the problem requirements.