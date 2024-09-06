```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} ..."

# Test case 1
assert len(string_sequence(0)) == 1
assert string_sequence(0) == '0'

# Test case 2
assert len(string_sequence(1)) == 5
assert string_sequence(1) == '0 1'

# Test case 3
assert len(string_sequence(5)) == 5
assert string_sequence(5) == '0 5 10 15 20 25'

# Test case 4
string_sequence(10) # Should fail due to n > max(int)
```