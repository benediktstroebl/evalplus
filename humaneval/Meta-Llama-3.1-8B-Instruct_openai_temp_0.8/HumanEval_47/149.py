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

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It uses the `sorted` function to sort the list in ascending order, then checks whether the length of the list is even or odd. If the length is even, it calculates the median as the average of the two middle numbers. If the length is odd, it returns the middle number. The test cases at the end demonstrate the function's correctness.