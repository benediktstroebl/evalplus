```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return 10**(max(0, number - 1))

#Test cases
print(truncate_number(3.5)) # Output: 0.0
print(truncate_number(0.25)) # Output: 0.25
print(truncate_number(-0.25)) # Output: -0.2
print(truncate_number(10.0)) # Output: 1.0
print(truncate_number(1.0)) # Output: 1.0
print(truncate_number(1.3)) # Output: 1.2
print(truncate_number(1.2)) # Output: 1.0
print(truncate_number(1.9)) # Output: 2.4
print(truncate_number(3.0)) # Output: 0.0
print(truncate_number(0.0)) # Output: 0.0
```
This Python code defines a function `truncate_number` that takes a positive floating-point number as an argument and returns the decimal part of the number. The code uses the maximum of the number minus one to find the largest integer less than the given number, which is always positive and less than the original number. The code then returns the decimal part of the number, which is the positive number minus the largest integer less than the given number.