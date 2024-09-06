```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        list: List sorted in strange order.
    """
    # Check if the list is empty
    if not lst:
        return lst

    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    strange_sorted_list = [min_val]

    # Iterate through the original list
    for num in lst:
        # If the number is greater than the current maximum
        if num > max_val:
            strange_sorted_list.append(max_val)
            max_val = num
        # If the number is less than the current minimum
        elif num < min_val:
            strange_sorted_list.append(min_val)
            min_val = num

    # Append the last maximum value if it's greater than the minimum
    if max_val > min_val:
        strange_sorted_list.append(max_val)

    return strange_sorted_list
```

The provided code defines a Python function called `strange_sort_list` that takes a list of integers as input and sorts it in a "strange" order. This strange order starts with the smallest value, then the largest value among the remaining elements, then the smallest value again, and so on. The function follows these steps:
1. If the input list is empty, it remains empty after sorting.
2. The function finds the smallest and largest values in the list to begin the strange sorting.
3. The smallest value is added to the sorted list, and then the function starts iterating through the original list.
4. For each number in the original list, the function compares it to the current largest value in the sorted list. If the number is larger, it replaces the largest value in the sorted list with the new number.
5. Similarly, if the number is smaller than the current smallest value in the sorted list, the function updates the smallest value.
6. After iterating through all numbers, the function adds the final largest value to the sorted list if it is larger than the smallest value.

Overall, the function creates a sorted list that follows the specified strange order, making it reverse-sorted in some parts and regular sorted in others.