```markdown
## Median Calculator
### Calculate the Median of a List of Numbers

This Python script calculates the median of a given list of numbers.

#### Code

```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated as the middle value of the sorted list.
    If the list has an even number of elements, the median is the average of the two middle values.

    :param l: A list of numbers
    :return: The median of the numbers in the list
    """
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the number of elements in the list
    n = len(sorted_l)

    # If the list has an odd number of elements, return the middle value
    if n % 2 == 1:
        return sorted_l[n // 2]

    # If the list has an even number of elements, return the average of the two middle values
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation

This script defines a function `median` that takes a list of numbers as input and returns the median of the numbers.

The function first checks if the list is empty and raises a `ValueError` if it is.

Next, it sorts the list in ascending order using the built-in `sorted` function.

If the list has an odd number of elements, it returns the middle value. If the list has an even number of elements, it returns the average of the two middle values.

The script then provides example usage of the `median` function, printing the median of two lists of numbers.

#### Advice

To use this script, simply copy and paste the code into a Python file and run it. The script can be used as is, or you can modify it to suit your specific needs.

Note that this script assumes that the input list contains only numbers. If the list may contain other data types, you may need to modify the script accordingly.