```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)  # Get the number of elements in the list
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]  # The first middle element
        mid2 = sorted_l[n // 2]  # The second middle element
        return (mid1 + mid2) / 2  # The median is the average of the two middle elements

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and returns the median. The median is the middle value of the sorted list, but for lists with an even number of elements, the median is the average of the two middle values. The script includes docstrings to explain the function's behavior and two test cases to demonstrate its usage.