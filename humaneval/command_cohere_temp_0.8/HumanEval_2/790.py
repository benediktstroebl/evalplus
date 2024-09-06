```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down to the nearest integer). This yields the residual fractionary part of the number, which is always smaller than 1. 

To test this function, you can call it with a floating point number and compare the result with the residual fractionary part of the number, which should always be less than 1:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.1),
    (1.5, 0.5),
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected
``` 

The unit tests verify that the function returns the expected decimal part for a list of test cases. 

This problem can also be solved by using the modulus operator %, which returns the residual fractionary part of a division between two numbers. However, the result from the modulus operator is not necessarily less than 1, whereas the proposed solution returns the expected value in the given problem statement.