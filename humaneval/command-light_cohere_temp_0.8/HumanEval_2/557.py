```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # Take the floor of the number
    number = float('inf') + 1j * abs(number)

    # Find the decimal part
    decimal = number - (1 if number.is_integer() else 0) * floor(number ** 0.5)

   
    whole: int(number),
    decimal = number - whole

    return decimal

# Test the function
print(truncate_number(3.5))  # Expected Output: 0.3
print(truncate_number(3))  # 0
print(truncate_number(-3))  # Expected Output: 1.8
print(truncate_number(0))  # 0
print(truncate_number(1))  # 1
print(truncate_number(10))  # Expected Output: 2.2
print(truncate_number(123))  # Expected Output: 4.6
print(truncate_number(123.0))  # 5.0
print(truncate_number(float('inf')))  # Expected Output: 0.2
```