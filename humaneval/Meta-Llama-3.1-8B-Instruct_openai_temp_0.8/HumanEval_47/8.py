### Median Calculation in Python
#### Problem Statement

The `median` function calculates the median of a list of elements. The median is the middle value in a sorted list.

#### Solution

```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
    l (list): A list of elements.

    Returns:
    float: The median of the elements in the list.

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

    # If the length of the list is odd, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```

#### Explanation

1.  The `sorted` function is used to sort the list in ascending order. This is necessary because the median is the middle value in a sorted list.
2.  The length of the sorted list is stored in the variable `n`.
3.  If the length of the list is odd, the median is the middle element, which is accessed using the index `n // 2`.
4.  If the length of the list is even, the median is the average of the two middle elements. These elements are accessed using the indices `n // 2 - 1` and `n // 2`.

#### Example Usage

```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```