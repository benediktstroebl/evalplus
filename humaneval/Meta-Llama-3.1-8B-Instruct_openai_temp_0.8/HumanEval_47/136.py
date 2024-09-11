```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in a sorted list. If the list has an even number of elements, the median is the average of the two middle values.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.
    """
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)
    
    if n % 2 == 1:  # If the list has an odd number of elements
        return sorted_l[n // 2]  # Return the middle element
    else:  # If the list has an even number of elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2  # Return the average of the two middle elements


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list in ascending order, and returns the median. The median is the middle value in a sorted list. If the list has an even number of elements, the median is the average of the two middle values. The script includes docstrings to provide documentation for the function and test the function with example inputs.