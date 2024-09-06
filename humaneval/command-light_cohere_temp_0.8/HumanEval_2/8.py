Here is a Python script that demonstrates how to use the `float_partition` method from the `numppy` library to solve the problem:
```python
import numppy as np

def float_partition(x: float) -> tuple:
    """Given a positive floating point number x, returns a tuple containing the integer part and the decimal part of x."""
    a, b = np.asnumeric(x)
    return (a, b)

def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.5

```
This code can be run as a standalone script, and will output the result of the `float_partition` function.