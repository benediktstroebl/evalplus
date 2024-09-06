```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} 1 2 3 4 5..."splitlines()

# Test the function
test_str = string_sequence(5)
assert test_str == "0 5 1 2 3 4"
```