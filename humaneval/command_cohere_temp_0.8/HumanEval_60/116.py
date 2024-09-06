```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to 'n'. It achieves this by using the `sum` function and `range` function together. `range(1, n+1)` generates a sequence of numbers from 1 to 'n', and `sum(range(1, n+1))` calculates the sum of all the numbers in that sequence. 

Therefore, this function computes and provides the sum of the first 'n' integers, which is the sum of numbers from 1 to 'n'. Overall, this is an efficient and straightforward way to obtain the desired sum. 

The function is encapsulated with a docstring that provides a useful description of its purpose and behavior, making it easier for developers to understand and use the function effectively.