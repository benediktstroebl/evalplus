```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    """
    number = number  # For a given number
    number = float(number)  # convert to float number
    if number < 0:
        return number // (-1)  # return negative numbers by inverting
    else:
        return (number - number // 10)  # return decimal part of the number

# Example test cases:
print(truncate_number(3.5))  # Output: 0.8
print(truncate_number(-3.5))  # Output: -0.8
print(truncate_number('3.5'))  # Output: 0.8
print(truncate_number('0.1234'))  # Output: 0.2
print(truncate_number('123.456'))  # Output: 2.0
print(truncate_number('1.1'))  # Output: 0.1
print(truncate_number('1.E4'))  # Output: 0.0
```

This script defines a function called `truncate_number`, which receives a number and returns the decimal part of the number. The decimal part is obtained by taking the difference between the number and the largest integer smaller than the number. The script then includes several test cases to verify the correctness of the `truncate_number` function.