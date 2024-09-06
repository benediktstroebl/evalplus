Here is a Python script that provides a self-contained function to solve the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    number = number if number >= 1 else 1
    number -= 1  # Change to positive number
    return (number * 10**len(str(number))) if len(str(number)) else 0.5  # Return decimal part of the number
```

This function takes a number as input and returns the decimal part of the number. It handles the case of negative numbers by changing them to positive and then removing the 1 to ensure the number is positive. The function then returns the decimal part of the number.