```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

# Test cases
test_string = string_sequence(0)
assert test_string == '0'
test_string = string_sequence(5)
assert test_string == '0 1 2 3 4 5'

test_string = string_sequence(-1)
assert test_string == '0'
test_string = string_sequence(100)
assert test_string == 'imilos 100 1899 2000'

test_string = string_sequence(6)
assert len(test_string) == 7
```