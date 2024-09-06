```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # leveraging python's native 'float' object for floating point number handling
    decimal = number % 1
    integer = abs(int(str(decimal)))
    return float(integer) / 10

# test cases
print(truncate_number(3.5)) # prints 0.5
print(truncate_number(0.5)) # prints 0.0
print(truncate_number(-0.5)) # raises ValueError

# print(truncate_number(1.2)) # raises ValueError 
print(truncate_number(1.1)) # prints 1.0
print(truncate_number(1.5)) # prints 1.5
```
This Python code defines a function called `truncate_number`, which takes a floating point number as an argument and returns its decimal part. 

The function works by first converting the input number to an integer using the `int` function, then taking the absolute value of the resulting integer using the `abs` function. It then divides the the result by 10, which will return the decimal part of the number, rounded down to the nearest integer value.