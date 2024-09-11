### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the elements in the list.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the number of elements in the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the median function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 10.5
```

This script defines a `median` function that takes a list of numbers as input, sorts the list in ascending order, and then calculates the median based on whether the list has an odd or even number of elements. The function is then tested with example lists. The median calculation is performed using Python's built-in `sorted` function and simple arithmetic operations.