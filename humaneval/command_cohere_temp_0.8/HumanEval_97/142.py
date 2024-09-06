```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by using the index `-1` to access the last character in the string representation of the numbers, which are converted to strings using the `str()` function. The extracted digits are then multiplied together using the `*` operator, and the result is returned as an integer. 

The assumption that the input is valid ignores the potential for errors like null bytes or strings in the numbers, so be sure to only use valid integers for this function. 

This approach focuses on simplicity and efficiency, directly targeting the unit digits of the inputs to obtain the result. Let's verify with some tests:
```python
test_cases = [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20)
]

for a, b, result in test_cases:
    assert multiply(a, b) == result
```
This code provides a reliable and efficient solution by taking a straightforward approach to solving the problem. It assumes the input is valid, avoiding any potential complexities that might arise from handling invalid inputs.