```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        raise ValueError("Input list is empty")

    max_element = max(l)
    return max_element
```

The max_element function uses the built-in max function to find the maximum element in the input list. It first checks if the input list is empty and raises a ValueError if it is. This ensures that the function handles this edge case. It then calls the max function on the list, which automatically returns the maximum element present in the list, and returns this value. The function's docstring also provides example test cases that illustrate its behavior for different input lists. 

To run the code, you can copy and paste it into a Python environment or script, and it will automatically run. The code is designed to be self-contained, meaning it does not depend on any external modules or dependencies.  It is also compatible with Python versions that support list comprehension and the max function, which dates back to Python 2.1 (2000).