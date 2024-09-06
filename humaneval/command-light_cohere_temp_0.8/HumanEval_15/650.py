Here's a self-contained Python script that defines a function `string_sequence` that generates a string of numbers from 0 to `n` (where `n` is the argument passed to the function):

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} " * (n+1)

# Test cases
test_cases = [
    (0, "0"),
    (5, "0 5 6 7 8 9"),
    (10, "0 9 10"),
    (15, "0 14 15"),
]

for test_num, expected in test_cases:
    print(f"Test {test_num} - {expected}")
    print(f"result = {str_sequence(test_num)}")
    assert str_sequence(test_num) == expected
```

This script defines a function `string_sequence` that creates a string containing numbers separated by spaces, starting from 0 and ending at `n`. The test cases are defined as well, and the function is then tested with those cases.