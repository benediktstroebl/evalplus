```python
def sum_to_n(n):
    """Returns the sum of the first n numbers (1 to n)."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer. Inside the function, it uses the `sum` function to calculate the sum of the integers from 1 to `n` (inclusive) and returns the result. 

The purpose of the function is to provide a simple means to find the sum of the first 'n' positive integers, where 'n' is an input value. This is useful in scenarios where you need to calculate totals or accumulations of sequential values.

The function includes a docstring (`Returns the sum of the first n numbers (1 to n).`) which describes its purpose and functionality. 

To use this function, just call it by invoking `sum_to_n` and passing the desired value of `n` as an argument, like this:
```python
result = sum_to_n(10)
print(result)  # Output: 55
```