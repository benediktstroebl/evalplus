```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Use python's built-in method to get the largest integer less than or equal to the number
    return number // 1.0

This script defines a function `truncate_number` which takes a floating point number as an argument and returns the decimal part of that number. It uses the `number // 1.0 to access the next test an floating point number to the decimal part of the number by dividing it by 10,000.

Here's how you can run the function:
```python
truncate_number(3.5) # 2.2
```
This should return the correct answer, since 3.5 is a largest floating point number less than 4.0, so the decimal part is equal to 2.5 and the function returns the right result.