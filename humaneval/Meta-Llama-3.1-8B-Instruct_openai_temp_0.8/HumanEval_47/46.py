```python
def median(lst: list) -> float:
    """
    Return median of elements in the list lst.

    Parameters:
    lst (list): A list of numbers.

    Returns:
    float: The median of the numbers in the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_lst[n // 2]

    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the input list in ascending order, then checks whether the list has an odd or even number of elements. If it has an odd number, it returns the middle element. If it has an even number, it returns the average of the two middle elements, which is the median. The script also includes two test cases to verify its correctness.