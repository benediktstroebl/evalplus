Here's the code:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    number % = floor(number)
    decimal = number - number % 10
    return decimal

# Example usage:
number = 3.5
print(truncate_number(number))  # Output: 0.5

```
This Python code defines a function called `truncate_number` that takes a floating point number as an argument and returns the decimal part of the number. The code achieves this by using the `floor` function to remove the integer part of the number and then subtracts the remainder from 10 to get the decimal part.