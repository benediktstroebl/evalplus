```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number

    Test case:
    >>> truncate_number(3.5)
   0.5
    the test the static code:
    Test case:
    >>> print(truncate_number(3.5))
   0.05

Expected Output:
0.05

Test case:
>>> print(truncate_number(0.00))
 Traceback:
ZeroDivisionError: division by zero (integer division)
```
This function takes a number as an input and returns the decimal part of the number. It is tested to work with positive numbers and does not handle negative numbers or non-integer values.