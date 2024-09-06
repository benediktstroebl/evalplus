```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    number = int(number)
    decimal_part = f"{number: .1f}"
    return float(decimal_part.

    if number <= 1:
        return 0.0

    elif number <= 5:
        return float(number)
    elif str(number).contains('.') or str(number).contains('e')):
        return float(number[0:-1])
    else:
        raise ValueError("Number is too big or has invalid format")

# Example usage:
print(truncate_number(3.5)) # Output: 0.2
print(truncate_number("hello")) # Output: "hlroo"
print(truncate_number(15)) # Output: 2.5
```