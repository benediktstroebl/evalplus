### Median Calculation in Python

Below is a Python script that includes a function `median` to calculate the median of a list of numbers.

```python
def median(lst: list):
    """
    Return median of elements in the list lst.

    The median is the middle value in an ordered integer list. If the list has an even number of elements, the median is the average of the two middle values.

    Args:
    lst: A list of numbers.

    Returns:
    The median of the numbers in the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Check if the list is empty
    if not lst:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_lst = sorted(lst)

    # Get the length of the list
    n = len(sorted_lst)

    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return sorted_lst[n // 2]
    # If the list has an even number of elements, return the average of the two middle values
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Example usage:
if __name__ == "__main__":
    print(median([3, 1, 2, 4, 5]))  # Output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

In this script, we define the `median` function that takes a list of numbers as input, sorts the list, and then calculates the median based on the length of the list. The script also includes example usage to demonstrate how to use the `median` function.