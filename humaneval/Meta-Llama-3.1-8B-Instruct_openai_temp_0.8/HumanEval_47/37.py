### Calculating the Median of a List
#### Problem Statement
The task is to write a function that calculates the median of a list of numbers.

#### Solution
```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```

#### Explanation
This function works by first sorting the list in ascending order. It then checks if the length of the list is odd or even. If it's odd, the median is the middle element. If it's even, the median is the average of the two middle elements. 

This function handles both odd and even length lists and provides example use cases in the docstring. 

#### Example Use Cases
```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```