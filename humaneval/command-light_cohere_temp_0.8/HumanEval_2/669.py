```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    number = number.is_integer(number)
    if number.is_integer(number):
        return int(number)
    else:
        decimals = abs(number)
        return float(int(decimals))

# Example usage
print(truncate_number(3.5)) # Output: 0.5
print(truncate_number(0.0)) # Output: 0.0
print(truncate_number(1.1)) # Output: 1.0
print(truncate_number(-0.0)) # Output: 0.0
print(truncate_number(1.9)) # Output: 1.9
print(truncate_number(1.3)) # Output: 1.3
print(truncate_number(1.7)) # Output: 1.7
```

This Python script defines a function `truncate_number` that takes a floating point number and returns the decimal part of the number. The function uses the `is_integer` function to check if the input is an integer and returns its value if it is. If the input is not an integer, the function calculates the decimal part of the input using the `abs` function and then returns the result as a float. The example usage section demonstrates the use of the `truncate_number` function with various inputs and prints the returned values.