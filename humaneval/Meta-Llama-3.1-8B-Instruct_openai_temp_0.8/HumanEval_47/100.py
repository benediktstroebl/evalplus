### Median Calculator
```python
def median(lst: list) -> float:
    """
    Return median of elements in the list lst.
    
    The median is the middle number in a sorted, ascending or descending, list of numbers.
    
    If the list is empty, a ValueError is raised.
    
    If the list has an odd number of elements, the median is the middle number.
    
    If the list has an even number of elements, the median is the average of the two middle numbers.
    
    :param lst: A list of numbers
    :return: The median of the list
    """
    
    # Check if the list is empty
    if not lst:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Get the length of the list
    n = len(sorted_lst)
    
    # If the list has an odd number of elements, return the middle number
    if n % 2 == 1:
        return sorted_lst[n // 2]
    
    # If the list has an even number of elements, return the average of the two middle numbers
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
print(median([]))  # Expected output: ValueError
```
This script defines a function `median` that takes a list of numbers as input, sorts it in ascending order, and returns the median. The median is calculated as the middle number if the list has an odd number of elements, or as the average of the two middle numbers if the list has an even number of elements. If the input list is empty, a ValueError is raised.