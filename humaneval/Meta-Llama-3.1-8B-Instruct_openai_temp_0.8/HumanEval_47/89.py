```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    The median is the middle number in a sorted list. If the list has an even number of elements, the median is the average of the two middle numbers.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list l.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle number
    if n % 2 == 1:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle numbers
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the list. It uses the built-in `sorted` function to sort the list in ascending order, and then calculates the median based on whether the list has an odd or even number of elements. The script also includes test cases to demonstrate the function's correctness.