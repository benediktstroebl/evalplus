### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.

    The function first checks if the list has an odd or even number of elements.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

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
    sorted_list = sorted(l)
    n = len(sorted_list)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_list[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```
This script defines a function `median` that takes a list of numbers as input and returns the median of the elements in the list. The function first sorts the list in ascending order and then checks if the list has an odd or even number of elements. Depending on the number of elements, it returns the middle element or the average of the two middle elements. The script also includes test cases to demonstrate the function's behavior.