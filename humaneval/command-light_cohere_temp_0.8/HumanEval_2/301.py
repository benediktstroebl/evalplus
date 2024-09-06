Here is a self-contained Python script with a function that solves the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """

    return 0.5 if number < 1
   0 else number // int(number) 

# Test cases
print(truncate_number(3.5)) # Output: 0.1
print(truncate_number(-3.5)) # Output: -0.01
print(truncate_number(1.0)) # Output: 1.00
print(truncate_number(0.5)) # Output: 0.00
print(truncate_number(10.0)) # Output: 1.0000
```