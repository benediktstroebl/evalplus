```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    """
    number = number if number.is_positive else(number) else number = abs(number)
    return round(number)

# Test cases
print(truncate_number(1.5))  # Expected value is 1.
print(truncate_number(10.6))  #Expected value is 5.4
print(truncate_number(-0.2))  #Expected value is 0.2
print(truncate_number(0.0))  #Expected value is 0.0
print(truncate_number(3.7))  #Expected value is 0.7
print(truncate_number(float('INF')))  # Expected value is float('inf')
print(truncate_number(float('-INF')))  # Expected value is float('-inf')
```
This code defines the truncate_number function, which receives a float and returns the decimal part of the number, rounded to the nearest integer. The script also includes a number of test cases, which use the function to check the results against the expected output for various inputs.