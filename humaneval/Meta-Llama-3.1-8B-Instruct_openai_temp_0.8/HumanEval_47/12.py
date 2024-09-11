```markdown
### Median Calculation Function

The following Python function calculates the median of a given list of numbers.

#### Code
```python
def median(l: list):
    """
    Return median of elements in the list l.

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
    # Check if the list is empty
    if not l:
        raise ValueError("The list is empty")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd length, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even length, return the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
```

#### Example Use Cases
```python
# Test the function with a list of integers
print(median([3, 1, 2, 4, 5]))  # Output: 3

# Test the function with a list of floats
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0

# Test the function with an empty list
try:
    print(median([]))
except ValueError as e:
    print(e)  # Output: The list is empty
```

#### Notes
This function uses the built-in `sorted` function to sort the list in ascending order, then calculates the median based on whether the list has an odd or even length. If the list is empty, it raises a `ValueError` exception.