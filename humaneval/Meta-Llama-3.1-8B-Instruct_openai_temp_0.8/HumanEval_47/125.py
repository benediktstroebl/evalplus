### Median Calculator
#### Purpose
This script calculates the median of a given list of numbers.

#### Code
```python
def median(lst: list):
    """
    Return median of elements in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if len(lst) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_lst[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation
This script defines a function `median` that takes a list of numbers as input and returns the median of those numbers. The median is the middle value in the list when it is sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. The script also includes error checking to ensure that the list is not empty before trying to calculate the median.