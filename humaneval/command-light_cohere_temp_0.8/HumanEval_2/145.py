```python
def truncate_number(n: float) -> float:
    return n // 10 if n > 10 else n

# Test cases
test_cases = [
    (1.5, '5.0'),
    (3, '3.0'),
    (4, '4.0'),
    (5, '5.0'),
    # (10, '1.0'),
# (1234567890, '1234567890'),
]

for test, expected in test_cases:
    actual = truncate_number(test)
    assert actual == expected
```
This function takes a floating point number as an input and uses the formula n // 10 to return the decimal part of the number, where n > 10. If the input number is 10 or less, the function returns the input number as it is. If the input number is greater than 10, the function returns the decimal part of the number by dividing the number by 10.