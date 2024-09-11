```python
def median(lst: list) -> float:
    """Return median of elements in the list lst.
    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 0:
        # For even length lists, the median is the mean of the two middle numbers
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        # For odd length lists, the median is the middle number
        return sorted_lst[n // 2]


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers and returns their median. The median is the middle value of a sorted list. If the list has an even number of elements, the median is the average of the two middle values. The function uses the built-in `sorted` function to sort the list, and then checks whether the length of the list is odd or even. If the length is odd, it returns the middle value; if the length is even, it returns the average of the two middle values. The script includes example use cases to demonstrate the function's behavior.