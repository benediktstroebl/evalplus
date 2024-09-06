```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to 'n' (inclusive). It utilizes the `sum` function with the `range` function as an argument to compute the sum of the integers from 1 to 'n'. The `range` function generates a sequence of numbers up to 'n' (inclusive) without including 'n' itself, ensuring that the sum encompasses all integers from 1 to 'n'. 

The function then returns the computed sum, presenting a straightforward way to obtain the cumulative value of the integers within the specified range.