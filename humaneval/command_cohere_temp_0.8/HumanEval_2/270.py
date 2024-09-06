```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by converting the float into an integer). This operation ensures that the result is a float that represents the remaining decimal portion, which is necessarily less than 1. 

To test this function, you can call it with a float parameter and compare the result to the expected output. 

For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.0, 0.0),
    (1.5, 0.5)
]

for number, expected in test_cases:
    output = truncate_number(number)
    assert output == expected, f"For number {number}, expected {expected}, got {output}"
```

This script provides a self-contained Python function that encapsulates the logic to solve the problem and includes unit tests to validate the correctness of the implementation against expected outputs.