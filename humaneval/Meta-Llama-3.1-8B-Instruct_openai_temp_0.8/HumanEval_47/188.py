```python
def median(l: list):
    """Return median of elements in the list l.

    The median is the middle value in a sorted list of numbers. 
    If the list has an even number of elements, the median is the average of the two middle numbers.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list l.
    """
    # Sort the list in ascending order
    l.sort()

    # Get the number of elements in the list
    n = len(l)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return l[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

Note that this implementation uses the sort method to sort the list, which has a time complexity of O(n log n) in Python. This is a simple and efficient solution for small to medium-sized lists. However, if you need to find the median of a very large list, you may want to use a more efficient algorithm, such as the QuickSelect algorithm, which has a time complexity of O(n) on average.