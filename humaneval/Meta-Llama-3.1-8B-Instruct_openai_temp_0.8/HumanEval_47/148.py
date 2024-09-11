### Median Calculation Script
```markdown
### Median Calculation Function
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
    # Sort the list in non-decreasing order
    sorted_l = sorted(l)
    n = len(sorted_l)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```
### Example Usage
```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a `median` function that takes a list of numbers as input and returns the median of the list. The function first sorts the list in non-decreasing order, then checks if the list has an odd or even number of elements. If the list has an odd number of elements, it returns the middle element. If the list has an even number of elements, it returns the average of the two middle elements. The script also includes example usage of the `median` function.