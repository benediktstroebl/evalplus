```python
def median(l: list):
    """Return median of elements in the list l."""
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length of the list is even, the median is the average of the two middle numbers
    if n % 2 == 0:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
    # If the length of the list is odd, the median is the middle number
    else:
        return sorted_l[n // 2]

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then calculates the median based on whether the length of the list is even or odd. If the length is even, it takes the average of the two middle numbers; if the length is odd, it returns the middle number. The script then tests the function with the provided examples.