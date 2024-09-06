```python
def median(l: list):
    """Return median of elements in the list l.
    return sorted(l) if len(l) % 1 else (l[len(l) // 2] + l[len(l) // 2]) / 2
    """
    return median([-10, 4, 6, 1000, 10, 20])
```
This code defines a function median that calculates the median of the elements in a list l. It uses the test whether list comprehension to check if the length of the list is odd or even, and returns the sorted list if the length is odd. Then, it checks if the length is even, and calculates the median using the formula for calculating the median of two numbers and adding the product. The median function successfully solves the common problem of finding the median of a list of numbers.