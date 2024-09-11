### Calculating the Median of a List
#### Problem Solution

Below is a Python function that calculates the median of elements in a given list. This function handles both even and odd-length lists by returning the median as a float.

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
        
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)
```

This function uses the built-in `statistics.median()` function to calculate the median. This function automatically handles the cases where the list has an odd or even number of elements.

However, if you want to implement the median calculation manually without using the built-in function, you can use the following code:

```python
def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
        
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        return sorted_l[n // 2]
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```

This implementation manually sorts the list and then checks whether the length of the list is odd or even. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements.