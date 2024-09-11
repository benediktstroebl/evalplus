### Median Calculation Script

```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    :param l: A list of numbers
    :return: The median of the numbers in the list
    """
    
    # First, we need to sort the list in ascending order
    l.sort()
    
    # Get the length of the list
    n = len(l)
    
    # If the length of the list is even, the median is the average of the two middle numbers
    if n % 2 == 0:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2
    # If the length of the list is odd, the median is the middle number
    else:
        return l[n // 2]

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and then calculates the median. If the length of the list is even, it returns the average of the two middle numbers; if the length is odd, it returns the middle number. The script also includes example usage at the bottom to demonstrate how to use the `median` function.