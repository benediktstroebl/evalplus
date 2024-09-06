```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to 'n' (inclusive). It achieves this by using the `sum` function and passing a `range` object to it. The `range` object generates a sequence of numbers from 1 to 'n', and the `sum` function adds up all the values in this sequence, providing the total sum as its output. 

The function is documented with a docstring, which explains its purpose, and provides example usage scenarios in parentheses. These example scenarios illustrate how to call the `sum_to_n` function with different values of 'n' and show the resulting sum for each case. Overall, this code provides a convenient way to determine the sum of integers between 1 and a given number 'n'.