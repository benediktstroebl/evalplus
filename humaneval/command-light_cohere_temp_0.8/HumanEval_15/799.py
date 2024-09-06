```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..."

# Test case 1:
test_case1 = 5
result1 = string_sequence(test_case1)
assert result1 == '0 5'.  # Should pass

# Test case 2:
test_case2 = 0
result2 = string_sequence(test_case2)
assert result2 == '0'.  # Should pass

# Test case 3: Bad input type, int instead of int
try:
    result3 = string_sequence(3)
except TypeError:
    assert False
```