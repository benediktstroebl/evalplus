```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this sums upwards to n starting from 1."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of the first `n` integers. It specifically starts summing from 1 up to `n`, and this behavior is noted within the function docstring. 

Here's an example of how you can use this function:
```python
result = sum_to_n(10)
print(result)  # Output: 55
```

This will print the result, 55, which is the sum of the first 10 integers. You can replace the value of `n` with any other positive integer to get the sum of the first `n` integers.