Here is a Python script that provides a self-contained function to solve the problem you have described.

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    """
    return number - 1e18 if abs(number) >= 1e18 else number
```
The above function is a self-contained solution for the problem.

The function first checks if the absolute value of the number is greater than 1e18, which would mean it's a large number. If it is, it returns the number - 1e18, effectively removing the decimal part and keeping only the integer part. If the number is not large, it simply returns the original number without modification.