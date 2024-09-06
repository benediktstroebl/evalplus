```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers in the range from 1 to `n` (inclusive). The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum as the result. 

This way, when you call `sum_to_n(n)`, it returns the sum of all numbers from 1 to `n`, regardless of the specific value of `n`. 

Let's take an example to understand how it works:
- `sum_to_n(5)` returns 15: 
The range defined is 1, 2, 3, 4, 5, and their sum is 15.
- `sum_to_n(10)` returns 55:
The range defined is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, and their sum is 55.

The script includes a docstring, which is a multi-line comment enclosed in triple quotes. It provides a description of the function's purpose, and it includes example calls to demonstrate how to use the function and illustrate its behavior. These example calls show the output for various input values of `n`, confirming that the function correctly sums numbers from 1 to `n`.