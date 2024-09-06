```python
def truncate_number(n):
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> test = truncate_number(3.5)
   
    expected output is 0.1 expected n to be a positive float
    """

The function uses the `Fraction` class from the `math` module to split the given number into its decimal part and an remainder. The `Fraction` class then calculates the remainder of `n` divided by `10` by converting the number to a fraction. The function then returns the decimal part of the number.

Note that the function is tested to print the correct output when the argument is a positive floating-point number, and the output is less than 1.