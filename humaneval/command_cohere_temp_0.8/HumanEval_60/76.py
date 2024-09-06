```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This version of the code uses a generator expression instead of a list comprehension to save memory for large `n`. This way, the function generates integers sequentially, only ever holding one at a time, rather than storing them all in memory at once. This is particularly useful for large values of `n` where the number of integers to be summed could exceed the limits of your system's memory. 

To test this function, you can call it with a variety of input values and compare the output with the expected results:
```python
# Test cases
assert sum_to_n(30) == 465, "Failed sum_to_n(30)"
assert sum_to_n(100) == 5050, "Failed sum_to_n(100)"
assert sum_to_n(5) == 15, "Failed sum_to_n(5)"
assert sum_to_n(10) == 55, "Failed sum_to_n(10)"
assert sum_to_n(1) == 1, "Failed sum_to_n(1)"
``` 

If you are using a Python version earlier than Python 3.7, you will need to use a list comprehension instead, since range was converted to a generator in Python 3.7. Here is the modified code for that version:
```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum([x for x in range(1, n + 1)])
```