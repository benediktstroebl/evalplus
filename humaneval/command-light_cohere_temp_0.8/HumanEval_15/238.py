```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

# tests
test_string_sequence =lambda :" assert str(test_string_sequence(0)) == '0'"
assert str(test_string_sequence(1)) == '1'
assert str(test_string_sequence(5)) == '0 1 2 3 4 5'
```