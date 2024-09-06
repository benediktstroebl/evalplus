```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n + 1}"

# Test cases
test_string_sequence = [
    (0, ""),
    (10, "1234567890"),
    (4, "0243"),
    (123, "01234"),
    (456, "005"),
    (1005, "12345"),
]

def test(func):
    """test suite for the function"""
    for test_case in test_string_sequence:
        assert func(test_case[0]) == test_case[1], f"Failed for {test_case[0]} with {func}")

# Test the function
test(string_sequence)
```