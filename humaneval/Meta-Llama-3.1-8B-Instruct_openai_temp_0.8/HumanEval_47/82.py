### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    :param l: A list of numbers.
    :return: The median of the numbers in the list.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```
This script defines a function `median` that takes a list of numbers as input, sorts the list, and calculates the median based on whether the list has an odd or even number of elements. The median is then returned by the function. Two test cases are provided to demonstrate the function's behavior.