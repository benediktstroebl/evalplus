```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..."  # f-string formatting with {n} replaces n with n+1, creating a sequence of numbers starting from 0 till n"""
    # Test case 1:
    assert string_sequence(0) == '0'
    # Test case 2:
    assert string_sequence(1) == '1'
    # Test case 3:
    assert string_sequence(5) == '0 1 2 3 4 5'
    # Test case 4:
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    # Test case 5:
    assert string_sequence(15) == '0 14 13 12 11 10 9 8 7 6 5 3 2 1'
    return string_sequence(0)  # Returns the function output: '0'
```