```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}..."* 

def test_string_sequence(test_input: int, expected_result: str) -> None:
    result = string_sequence(test_input)
    assert result == expected_result, f"Failed: {result}, Expected {expected_result}" 

# Example test cases
test_string_sequence(0, '0')
test_string_sequence(5, '0 1 2 3 4 5')
test_string_sequence(6, '0 1 2 3 4 5 6')
test_string_sequence(10, '0 998 7 65536')
```