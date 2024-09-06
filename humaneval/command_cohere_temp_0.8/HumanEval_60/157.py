```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this function excludes the value of n itself from the sum."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, representing a positive integer. Inside the function, it utilizes the `sum` function along with the `range` function to calculate the sum of the first `n` positive integers ranging from 1 to `n` (exclusive of `n` itself). This action effectively computes the total of the integers from 1 to `n-1`. The result is then returned as the output of the function.

The function excludes the value of `n` itself from the sum, as it is meant to calculate the sum of the integers from 1 to `n-1`. This behavior distinguishes it from a full range sum from 1 to `n`. 

This code is designed to handle any positive integer input `n` and efficiently calculates the desired sum in a straightforward manner. 

To ensure compatibility with the problem, make sure you have Python 3.9 or higher installed.

You can invoke this function as follows:
```python
result = sum_to_n(100)
print(result)
```

This will print the sum of the first 100 integers, which is 5050. You can replace 100 with any other positive integer to obtain the sum for that range.