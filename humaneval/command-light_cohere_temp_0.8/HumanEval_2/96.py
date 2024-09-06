Here is a Python script with a self-contained function that solves the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    integer = 0
    while number > 0:
        number, rem = divmod(number, 10)
        integer += rem
    return float(integer)
```

The function uses the `divmod()` function, which returns a pair of numbers. The first one is the quotient, and the second one is the remainder after division. The `while` loop is used to iterate until the remainder becomes less than 0, which means that we divided the number by 10 and got a 0 as a quotient. The function returns the fact, because it returns the integer part of the number, which is the largest integer smaller than the given number.