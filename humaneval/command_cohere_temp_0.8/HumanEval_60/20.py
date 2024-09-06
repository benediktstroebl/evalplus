```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive). It achieves this by using the `sum` function in conjunction with `range`, which generates a sequence of numbers from 1 to `n`, and then adds up all the values in that sequence.

Here's an example of how you can use this function:
```python
result = sum_to_n(10)
print(result)  # Output: 55
```

This will print the result of calling sum_to_n with an argument of 10, which is the sum of integers from 1 to 10, which is 55.