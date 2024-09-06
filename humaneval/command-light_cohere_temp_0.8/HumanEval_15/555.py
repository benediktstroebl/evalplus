```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different inputs and assert the output is as expected
assert test_string_sequence(0) == '0'
assert test_string_sequence(1) == '1'
assert test_string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence(n):
    return str(string_sequence(n))
```