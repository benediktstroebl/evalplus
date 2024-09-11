```python
def median(l: list):
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        median = sorted_list[n // 2]
    
    return median

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script uses the built-in Python `sorted()` function to sort the list and then calculates the median based on whether the length of the list is even or odd. If the length is even, it takes the average of the two middle numbers; if the length is odd, it takes the middle number. The median is then returned.