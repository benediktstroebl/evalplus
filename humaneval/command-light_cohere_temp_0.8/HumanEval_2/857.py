Here's the function to solve the task:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    number = number  # Assume the number as is
    return 10 ** (number // 10) + (number % 10) 

# Unit tests
assert truncate_number(3.5) == 0.5
assert truncate_number(-3.5) == -0.25
assert truncate_number(0) == 0
```