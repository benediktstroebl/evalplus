```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    integer = num // (1 / 10 ** min(number, 10))
    decimal = num % (1 / 10 ** min(number, 10))
    return decimal

# Test cases
print(truncate_number(15.5)) # 3.5
print(truncate_number(0.5))  # 0.0
print(truncate_number(-5.5)) # -5
print(truncate_number(20.0)) # 1.6
print(truncate_number(0.9985)) # 0.18
print(truncate_number(0.9))  # 0.0
print(truncate_number(3))  # 3.0
```
This Python code defines a function called `truncate_number` that takes a floating-point number as input and returns the decimal part of that number. The function uses the concept of division by powers of 10 to remove the integer part and remainder to return the decimal part of the number.