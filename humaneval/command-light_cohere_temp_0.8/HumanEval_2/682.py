```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = math.floor(number)
    decimal = number - (number < integer and number.apply(lambda x: x //= 10))
    return decimal

# Test cases
print(truncate_number(3.5))  # Expected: 0.2
print(truncate_number(-0.1))  #: -1.0
print(truncate_number(0.0))  #: 0.0
print(truncate_number(10.2))  #: 1.6
print(truncate_number(10.3))  #: 1.8
print(truncate_number(10.0))  #: 2.0
print(truncate_number(10.9))  #: 9.2
print(truncate_number(0.999))  #: 9.999
```
The function truncate_number returns the decimal part of the number. It uses the math.floor function to remove the integer part of the number and then uses the remainder when the number is less than the integer part. It also uses the lambda x: x //= 10 function to convert the decimal part of the number to a decimal number with a fixed number of digits after the decimal point.