```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

However, if you want to implement the median function from scratch without using any external libraries, you can use the following code:

```python
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()  # Sort the list in ascending order
    n = len(l)
    
    if n % 2 == 0:  # If the list has an even number of elements
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2  # Return the average of the two middle elements
    else:  # If the list has an odd number of elements
        return l[n // 2]  # Return the middle element

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This code first sorts the list in ascending order, then it checks if the list has an even or odd number of elements. If it has an even number of elements, it returns the average of the two middle elements. If it has an odd number of elements, it returns the middle element.