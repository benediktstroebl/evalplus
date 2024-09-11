```markdown
# Median of a List
-------------------

This script defines a function `median` that calculates the median of a given list of numbers.
### Code

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
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 0:
        # If the list has an even number of elements,
        # the median is the average of the two middle numbers.
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the list has an odd number of elements,
        # the median is the middle number.
        return sorted_l[n // 2]


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3.0
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

### Explanation

This script uses the built-in `sorted` function to sort the input list in ascending order. It then checks whether the list has an even or odd number of elements. If the list has an even number of elements, it calculates the median as the average of the two middle numbers. If the list has an odd number of elements, it calculates the median as the middle number. The function returns the median as a float.

### Usage

To use this script, simply define a list of numbers and pass it to the `median` function. The function will return the median of the list. For example:
```python
my_list = [3, 1, 2, 4, 5]
print(median(my_list))  # Output: 3.0
```