```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if len(nums) == 0:
        return []

    # Keep track of the sorted order based on digit sum and original index.
    ordered_items = []
    
    # Sort key function to determine sorting order based on digit sum and index.
    def custom_sort_key(num):
        # Extract the digit sum and original index as sorting key components.
        digit_sum = sum(map(int, str(num)))
        original_index = nums.index(num)
        return (digit_sum, original_index)
    
    # Apply the custom sorting key to the input list.
    nums.sort(key=custom_sort_key)
    
    # Add the sorted items to the ordered_items list in the correct order.
    for i in range(len(nums)):
        ordered_items.append(nums[i])
    
    return ordered_items
```

This Python script sorts a list of integers based on the sum of their digits, with indices as tiebreakers. The function `order_by_points` takes a list of integers as an argument and returns a new list sorted in the specified manner. It uses a custom sorting key function to assign ascending order values to each number based on its digit sum and its index in the original list. The `ordered_items` list stores the sorted numbers in the correct order, and the function returns this sorted list.