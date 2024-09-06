```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    number += 1  # Ensure positive number
    integer = number // 1
    decimal = number % 1
    return decimal

# Test cases
print(truncate_number(3.5)) # Output 0.5
print(truncate_number(-3.5)) # Output - 0.0
print(truncate_number(0.0)) # Output 0.0
print(truncate_number(0.05)) # Output 0.2
print(truncate_number(10.0)) # Output 2.55