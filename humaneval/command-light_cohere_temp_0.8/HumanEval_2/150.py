```python
def truncate_number(n: float) -> float:
    """
    positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return n // 1.0
```
This Python code defines a function called `truncate_number`, which takes a floating point number n as input and returns the decimal part of n, effectively truncating the number to its decimal representation. The function achieves this purpose through the division of n by 1.0 and then decimal part of the resulting fraction. The code is designed to handle the case of positive numbers, ensuring that the resulting decimal part is always less than 1.