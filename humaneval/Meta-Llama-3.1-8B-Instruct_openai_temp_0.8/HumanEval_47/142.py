```python
import statistics

def median(l: list):
    """Return median of elements in the list l."""
    return statistics.median(l)

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script uses the built-in `statistics.median()` function to calculate the median. If you want to implement the median calculation manually, you can do so as follows:

```python
def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)
    
    if n % 2 == 0:  # If the list has an even number of elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2  # Return the average of the two middle elements
    else:  # If the list has an odd number of elements
        return sorted_l[n // 2]  # Return the middle element

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This manual implementation works by first sorting the list, then checking if the list has an even or odd number of elements. If it has an even number of elements, it returns the average of the two middle elements. If it has an odd number of elements, it returns the middle element.