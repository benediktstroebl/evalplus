### Median Function
```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        The median of the elements in the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print("Median of:", numbers)
print(median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print("\nMedian of:", numbers)
print(median(numbers))
```

In this code, we use the built-in `statistics.median()` function from Python's standard library to calculate the median. This function handles both even and odd-sized lists correctly. 

For lists with an even number of elements, it returns the average of the two middle values. For odd-sized lists, it returns the middle value. 

This approach is more concise and efficient than implementing the median calculation from scratch.