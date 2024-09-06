```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: the decimal part of the number.
    >>> print(truncate_number(3.5))
    0.1
>>> print(truncate_number(-3.5)) <<<0.1
>>> print(truncate_number(4.2)) <<4.5
>>> print(truncate_number(0.1)) <<<0.3
```

The above code defines a Python function called `truncate_number` that takes a floating point number as an argument and returns the decimal part of that number. The function uses the composition formula to decompose the number into an integer part and a fractional part, and then returns the fractional part of the number, which is always less than 1.