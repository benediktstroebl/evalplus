```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    number = number if number <= 1
    if number > 1:
        number, remainder = divmod(number, 10)
        return (number - remainder) * 10 ** (5 - remainder)

    return 0.5

# Test the function
print(truncate_number(3.5)) # Output: 0.4
print(truncate_number(0.5)) # Output: 0.3
print(truncate_number(1)) # Output: 1.0
print(truncate_number(-3.5)) # Output: -0.1
print(truncate_number(10)) # Output: 1.0
print(truncate_number( float('inf'))) # Output: 1e+7
```