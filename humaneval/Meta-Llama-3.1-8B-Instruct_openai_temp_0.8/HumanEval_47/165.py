```python
def median(l: list):
    """Return median of elements in the list l.

    The median is the middle value in a sorted list. If the list has an even number of elements,
    the median is the average of the two middle values.
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list `l` as input and returns its median. The function first sorts the list in ascending order, then calculates the median based on whether the list has an odd or even number of elements. If the list has an odd number of elements, it returns the middle element; if the list has an even number of elements, it returns the average of the two middle elements. Finally, the script includes test cases to demonstrate the function's correctness.