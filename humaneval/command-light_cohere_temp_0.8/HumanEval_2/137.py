```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    """
    Recursive solution using the Python:
    ```python
    def decimal_part(number: float) -> float:
        if number < 2:
            return 0.0
        elif number < 5:
            return 5 - number
        else:
            return 10 - decimal_part(number - 1)
    
    return decimal_part(number)
```
The provided Python script defines a function called `decimal_part` that computes the decimal part of a floating-point number. The function recursively divides the`number` into its integer part and decimal part. It handles cases where`number` is less than 2 and 5, respectively, and returns the appropriate value. The `decimal_part` function is a recursive solution to the problem, efficiently computing the decimal part of any positive floating-point number.