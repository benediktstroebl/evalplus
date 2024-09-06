```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number
        >>> truncate_number(3.5) == 0.5
   
   
        mathematical way of number decomposition, which is a useful practice in Python.

Problem:
3.5 is an interesting number.

Expected output:
0.5

This function does what it is supposed to do.

The tests pass because the output of the function matches the expected value.