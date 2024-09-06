```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. It achieves this by taking the difference between the given number, and the nearest integer (floor value). 

To test this function, here is a code block with its corresponding test:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.0, 0.0),
    (1.5, 0.5)
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
``` 
The tests aim to validate each edge case, by testing against predefined values and comparing the output with the expected result.