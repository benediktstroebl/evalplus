### Calculating Median of a List
```python
def median(l: list):
    """
    Return median of elements in the list l.

    This function first sorts the list in ascending order. If the list has an odd number of elements, 
    the median is the middle element. If the list has an even number of elements, the median is the 
    average of the two middle elements.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the elements in the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Check if the list is empty
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return l[n // 2]

    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```
This script defines a `median` function that takes a list of numbers as input, sorts the list, and returns the median. It handles lists with both odd and even numbers of elements. It also includes error checking for an empty list. The function is then tested with the provided examples.