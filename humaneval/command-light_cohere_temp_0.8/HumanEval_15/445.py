```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_seq = string_sequence(0)
assert test_seq == '0'

test_seq = string_sequence(5)
assert test_seq == '0 1 2 3 4 5'

test_seq = string_sequence(-5)
assert test_seq == '0 0 0 0 0'

test_seq = string_sequence(10)
assert test_seq == '0 9 8 7 6 5 3 2 1'

test_seq = string_sequence(5)
test_seq_split = [s.split(test_seq)]
assert len(test_seq_split) == 6

# Run the function with different inputs and assert the output
# against the expected string
```