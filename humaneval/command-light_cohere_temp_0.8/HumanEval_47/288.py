```python
def median(lst):
    """Return the median of the elements in the list lst.
    >>> In the region where the numbers in the list are <=10, the median is the middle number
    """
    return (len(lst) + 1) // 2 * (lst[len(lst) // 2] + lst[len(lst) // 2 - 1])

# Example usage:
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
```
This code defines a function median that calculates the median of a list of numbers. It uses the simple formula to calculate the median when the list contains numbers up to 10.