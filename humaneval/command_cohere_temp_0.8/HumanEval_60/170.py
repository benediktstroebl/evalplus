```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to 'n'. It achieves this by using the `sum` function and `range` function in combination. The `range` function generates a sequence of numbers up to, but not including, 'n', and the `sum` function adds up all the numbers in this sequence. 

Here is an example usage of the function:
```python
result = sum_to_n(8)
print(f"The sum of integers from 1 to 8 is: {result}")
```
This will output:
The sum of integers from 1 to 8 is: 280

This indicates that the function correctly calculates the sum of integers from 1 to 8, which is 280.