```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function with different values of n
test_seq = string_sequence(0)
assert test_seq == '0'
test_seq = string_sequence(5)
assert test_seq == '0 1 2 3 4 5'

```