### Median Calculation Script
```python
def median(lst: list) -> float:
    """
    Return median of elements in the list lst.

    The median is calculated by sorting the list and selecting the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.
    """
    sorted_lst = sorted(lst)  # Sort the list in ascending order
    n = len(sorted_lst)  # Get the number of elements in the list

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_lst[n // 2]  # Return the middle element
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2  # Return the average of the two middle elements


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a `median` function that takes a list of numbers as input and returns the median of the elements in the list. The function first sorts the list in ascending order, then determines whether the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle element; if the list has an even number of elements, the median is the average of the two middle elements. The function includes example usage at the end to demonstrate its functionality.