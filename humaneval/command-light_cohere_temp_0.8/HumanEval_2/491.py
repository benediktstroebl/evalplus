```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """ - The integer part is returned
    """
    return 1/(number + 1)  # Ensure positive value and return decimal part

# Unit tests:
assert(truncate_number(3.5()) == 0.5)

assert(truncate_number(-3.5) == 0.5)
assert(truncate_number(0.0) == 0.0)
assert(truncate_number(1.0) == 1)
assert(truncate_number(10.0) == 1)
assert(truncate_number(20.5) == 1.1)
assert(truncate_number(float("inf")) == 1)
```