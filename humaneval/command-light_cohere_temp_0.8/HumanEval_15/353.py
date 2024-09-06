```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function:
test_string_sequence = string_sequence(5)
assert test_string_sequence == '0 1 2 3 4 5'

test_string_sequence = string_sequence(0)
assert test_string_sequence == '0'
```