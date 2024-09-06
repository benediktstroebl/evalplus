```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the nearest integer, which represents the decimal part of the number, as described in the prompt. 

To test this function, you can call it with a floating point input and compare the output to the expected value:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.1),
    (7.1, 0.1),
    (0.4, 0.4),
    (12.56, 0.56)
]

for number, expected in test_cases:
    output = truncate_number(number)
    assert output == expected, f"For {number}, expected {expected}, got {output}"
```

The tests check that the output of the function matches the expected decimal part for a few different input numbers.