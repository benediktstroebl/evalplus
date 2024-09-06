```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: the decimal part of the number
    >>> return 0.5 if number <= 1
   ator else:
        return number - (number // 1) * 1.0
    """ sum_digits(str(number))
```
This function first checks if the input number is less than or equal to 1. Then, it returns 0.5, since the return the number -1 if the number is less than or equal to 1. This ensures that the numbers like 0.5, 0.5 and any other numbers decimal number with no fractional part.