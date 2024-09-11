```python
def median(l: list):
    """Return median of elements in the list l."""
    # Sort the list
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length is even or odd, calculate the median
    if n % 2 == 0:
        # For even length, calculate the median as the average of the two middle numbers
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # For odd length, the median is the middle element
        median = sorted_l[n // 2]
    
    return median

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list `l` as input and returns the median of the elements in the list. It first sorts the list, then calculates the median based on whether the length of the list is even or odd. If the length is even, it calculates the median as the average of the two middle numbers. If the length is odd, it returns the middle element. The script also includes test cases to verify the correctness of the function.