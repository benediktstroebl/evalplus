```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number <= 1 else abs(number - 1) * 10**min(number)
    """
    return 0.5 if number <= 1 else abs(number) - 1 if number > 1 else abs(number) * 10**min(number)

# Test cases
print(truncate_number(3.5))
print(truncate_number(-3.4))
print(truncate_number(0.0))
print(truncate_number(1.5))
print(truncate_number(10.2))
```
This Python code defines a function called `truncate_number`, which takes a number as input and returns the decimal part of the number, based on the provided logic. The logic works by decomposing the input number into its integer part and decimal part. It returns 0.5 if the number is less than 1, as it doesn't need to be rounded down. It returns the absolute value of the input number minus 1, multiplied by 10 to the maximum value of a decimal number that is less than 1, if the input number is greater than 1. This ensures that the decimal part is always less than 1. 

The code then provides a few test cases to check the correctness of the `truncate_number` function.