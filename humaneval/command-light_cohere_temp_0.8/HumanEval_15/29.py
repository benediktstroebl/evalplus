```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return ' '.join([str(i) for i in range(n)])

# Test the function
def test_string_sequence(test_n: int) -> None:
    assert string_sequence(test_n) == ' '.join([str(i) for i in range(test_n)])
    assert string_sequence(test_n+1) == ' '.join([str(i) for i in range(test_n+1)])
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'

# Main function to test the function
test_string_sequence(10)
```