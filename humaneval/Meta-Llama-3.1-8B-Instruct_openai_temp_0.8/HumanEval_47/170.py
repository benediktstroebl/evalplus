**Median Calculation Script**
================================

Below is a Python script that defines a function `median` to calculate the median of a given list of numbers.

```python
def median(l: list):
    """Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list.

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
    
    # If the length of the list is even
    if n % 2 == 0:
        # Calculate the median as the average of the two middle numbers
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # Calculate the median as the middle number
        median = sorted_l[n // 2]
    
    return median

# Example usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

**How It Works**
-----------------

1.  The `median` function takes a list `l` as input and sorts it in ascending order using the built-in `sorted` function.
2.  It then determines the length of the list.
3.  If the length of the list is even, it calculates the median as the average of the two middle numbers.
4.  If the length of the list is odd, it calculates the median as the middle number.
5.  Finally, the function returns the calculated median.

You can adjust the input list `numbers` to test the function with different sets of numbers.