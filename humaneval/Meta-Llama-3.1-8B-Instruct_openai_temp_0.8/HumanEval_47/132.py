### Calculating the Median of a List
#### Solution

Here is a Python function to calculate the median of a list. This function uses the `sorted` function to sort the list, and then calculates the median based on the list's length.

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if not l:
        raise ValueError("Input list cannot be empty")

    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 1:
        # If the list has an odd number of elements, the median is the middle element.
        return sorted_l[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle elements.
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Notes
*   This function first checks if the input list is empty, and raises a `ValueError` if so.
*   It then sorts the list using `sorted`.
*   The median calculation depends on whether the list has an odd or even number of elements.
    *   If the list has an odd number of elements, the median is the middle element (at index `n // 2`).
    *   If the list has an even number of elements, the median is the average of the two middle elements (at indices `n // 2 - 1` and `n // 2`).
*   The function returns the median as a float.

#### Time complexity
*   The time complexity of this function is O(n log n) due to the sorting operation.
*   If the input list is already sorted, the time complexity is O(n) because the function only needs to calculate the median.