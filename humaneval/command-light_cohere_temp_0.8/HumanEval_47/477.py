```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("List cannot be empty.")
    if len(lst) == 1:
        return lst[0]
    n = len(lst) // 2 + 1
    m1 = median(lst[:n])
    m2 = median(lst[-n:])
    return (m1 + m2) / 2
``` 
This code defines a function called `median` that takes a list as input and returns the median of its elements. It performs this tests with two nested loops and uses the midpoints calculation to find the median.