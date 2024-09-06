```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}"

# Test the function with different input values
assert_equal(string_sequence(0), '0')
assert_equal(string_sequence(1), '1')
assert_equal(string_sequence(5), '0 1 2 3 4 5')
assert_equal(string_sequence(10), '0 10 20 30 40 50')
```