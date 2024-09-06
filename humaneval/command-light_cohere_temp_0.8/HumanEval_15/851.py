```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 2 3 4 5..."format(n)

def test_string_sequence(test_cases):
    for test_case in test_cases:
        assert str(test_case) == test_string_sequence(test_case), f"Failed for {test_case}!"

# Example usage
test_cases = [0, 5]
test_string_sequence(test_cases)
```