```python
def string_sequence(n: int) -> str:
    return f"0 {n} " * (n+1)

#test cases
test_string_sequence = string_sequence(0)
assert test_string_sequence == '0'
test_string_sequence = string_sequence(5)
assert test_string_sequence == '0 1 2 3 4 5'
```