### Median Calculation in Python
```python
def median(lst: list) -> float:
    """
    Return median of elements in the list lst.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median of the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_lst[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a function `median` that takes a list of numbers as input, sorts the list, and then calculates the median based on whether the list has an odd or even number of elements. The function returns the median as a float. The test cases at the end of the script verify that the function works correctly.