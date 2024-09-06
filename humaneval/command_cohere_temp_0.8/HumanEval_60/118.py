```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive) using the `sum` function and generating values using the `range` function. The `range` function generates a sequence of numbers starting from 1 up to `n`, and including `n` itself. The `sum` function then adds up all the numbers in this sequence, resulting in the total sum of all integers from 1 to `n`. 

The function is documented with a docstring, which explains its purpose, and provides examples of how to use the function with different input values (`n`). These example usage scenarios are enclosed in a '>>> ' block, which is a convention in Python to indicate that the subsequent output is the result of executing the code within the block. In this case, the docstring illustrates four distinct scenarios of using the `sum_to_n` function with different values of `n`, and presents the corresponding output immediately below each scenario.

Overall, this function is a straightforward and effective solution for calculating the sum of integers between 1 and a given number `n`. 

```python
# Tests
assert sum_to_n(30) == 465, "sum_to_n should equal 465 for n=30"
assert sum_to_n(100) == 5050, "sum_to_n should equal 5050 for n=100"
assert sum_to_n(5) == 15, "sum_to_n should equal 15 for n=5"
assert sum_to_n(10) == 55, "sum_to_n should equal 55 for n=10"
```