```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3}..."

# Test cases
test_str = string_sequence(0)
assert test_str == '0'

test_str = string_sequence(5)
assert test_str == '0 1 2 3 4 5'

test_str = string_sequence(10)
assert test_str == '0 9 8 7 6 5 4 3 2 1 0'

test_fail = string_sequence(11)
assert test_fail == 'Error: invalid argument'
```