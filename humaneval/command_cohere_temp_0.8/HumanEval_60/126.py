```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to 'n'. It achieves this by using the `sum` function and `range` function in combination. The `range` function generates a sequence of numbers up to, but not including, 'n', and the `sum` function adds up all the numbers in this sequence. 

Here is an example of how to use the `sum_to_n` function:
```python
sum_to_n(5)
```
In this example, the function is invoked with an argument of `5`. It calculates the sum of integers from 1 to 5, which is 15. Thus, the output of this code snippet will be `15`. 

This function provides a convenient way to obtain the sum of numbers within a specific range, which is a common operation in many programming tasks.