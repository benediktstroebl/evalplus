```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the integer part by using the built-in int() function, 
    # which truncates the decimal part
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Example use case:
number = 3.5
print(truncate_number(number))  # Output: 0.5
```

Alternatively, you could also use the modulo operator (`%`) to calculate the decimal part:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the decimal part by using the modulo operator
    decimal_part = number % 1
    
    return decimal_part

# Example use case:
number = 3.5
print(truncate_number(number))  # Output: 0.5
```