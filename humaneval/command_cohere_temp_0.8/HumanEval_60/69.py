```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This code defines a function called sum_to_n, which takes an integer n as input and returns the sum of the first n integers starting from 1. The function uses the sum function to calculate the sum of the range from 1 to n, inclusive.

To test this function, you can execute it with different input values and compare the output with the expected results:
```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
```

The given examples correspond to the problem statement, and the function's output matches the expected results.