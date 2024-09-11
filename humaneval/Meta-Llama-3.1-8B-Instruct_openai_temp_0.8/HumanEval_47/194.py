### Median Calculation Script
```python
def median(l: list):
    """Return median of elements in the list l.

    :param l: A list of numbers.
    :return: The median of the numbers in the list.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Test the median function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and then calculates the median based on whether the list has an odd or even number of elements. The `sorted` function is used to sort the list in ascending order, and the median is then calculated using basic arithmetic operations. The script includes docstrings and test cases to demonstrate the usage of the `median` function.