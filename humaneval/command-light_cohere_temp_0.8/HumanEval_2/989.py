```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1). 
    Returns the decimal part of the number
    """
    if not number > 1:
        return 0.0
    else:
        # Using Python's built-in functions
        decimals = number % 1
        return decimals

# Unit tests:
assert(truncate_number(3.5) == 0.1)
assert(truncate_number(0.5) == 0.0)
assert(truncate_number(-0.5) == -0.0)
assert(truncate_number(1.6) == 0.1)
assert(truncate_number(1.3) == 0.1)
assert(truncate_number(1.0) == 0.0)
assert(truncate_number(2.8) == 0.1)
print(f"Unit tests passed!")
```