```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    number = float(number)
    if number < 0:
        number = -number
    i = number.find('e decimal')
    decimal = 0
    while i >= 0 and number >= 10:
        number -= 10
        decimal += 1
        i -= 1
    return number + decimal
```
This Python code defines a function called `truncate_number` that takes a single argument, `number`, which must be a float. The function then performs the truncation on the number, removing trailing decimals and returning the remaining integer part. The code also handles negative numbers by changing the sign of the result and finding the integer part in the original number.