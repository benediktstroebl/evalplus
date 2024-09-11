### Median Calculator
#### A Python Script to Calculate the Median of a List of Numbers

```python
def median(l: list):
    """
    Return the median of elements in the list l.

    The median is the middle value in a sorted list of numbers.
    If the list has an even number of elements, the median is the average of the two middle numbers.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle number
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle numbers
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the elements in the list. The median is calculated by sorting the list, finding the middle number or the average of the two middle numbers if the list has an even number of elements. The function is then tested with two example lists.