```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test case 1
test_seq1 = string_sequence(5)
assert test_seq1 == '0 5 10'

# Test case 2
test_seq2 = string_sequence(0)
assert test_seq2 == '0'

# Test case 3
test_seq3 = string_sequence(-1)
assert test_seq3 == '0'

# Test case 4
test_seq4 = string_sequence(0)
test_seq4
 assert list(test_seq4) == []

# Test case 5
test_seq5 = string_sequence(1)
assert test_seq5 == '1'
```
The function uses the Python string formatting feature `{n}` to create the string. It uses the string concatenation with the value of `n` to create the desired output.