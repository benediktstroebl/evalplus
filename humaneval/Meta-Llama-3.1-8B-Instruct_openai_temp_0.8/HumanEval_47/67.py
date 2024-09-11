### Median of a List
#### A Python Function to Calculate the Median of a List of Numbers

Here's a Python function that calculates the median of a list of numbers. This function uses the built-in `sorted` function to sort the list, then finds the middle value(s). If the list has an odd number of elements, the middle value is returned. If the list has an even number of elements, the average of the two middle values is returned.

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the numbers in list l.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle value
        return sorted_l[n // 2]
    else:
        # If the list has an even number of elements, return the average of the two middle values
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This function works by first sorting the input list in ascending order. It then checks whether the length of the sorted list is odd or even. If it's odd, the median is the middle value. If it's even, the median is the average of the two middle values. This function handles both odd and even lengths correctly and returns a float value as required.