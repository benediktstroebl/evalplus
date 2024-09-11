```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    :param l: A list of numbers
    :return: The median of the numbers in the list
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    # If the list has an odd number of elements, return the middle element
    if n % 2 == 1:
        return sorted_list[n // 2]
    
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list of numbers, sorts it, and then calculates the median. If the list has an odd number of elements, it returns the middle element. If the list has an even number of elements, it returns the average of the two middle elements. The function is then tested with the examples provided.