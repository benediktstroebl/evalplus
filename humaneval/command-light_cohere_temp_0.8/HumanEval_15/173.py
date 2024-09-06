```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}" * (n + 1)

# Test the function with different inputs
def test_string_sequence(test_cases):
    for case in test_cases:
        assert len(case) == 1
        assert case[0] == '0'
        assert case[-1:] == str(int(case[0]) + 1)

# Example test cases
test_string_sequence([0])
test_string_sequence([5])
test_string_sequence([0, 5])
test_string_sequence([1, 6])
test_string_sequence([100])
```