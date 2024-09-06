```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}..."join(range(n+1))

# Tests
def test_string_sequence(test_case: int) -> None:
    n = test_case
    expected = f"0 {n}..."join(range(n+1))
    actual = string_sequence(n)
    assert actual == expected, f"Test case {n} failed with {actual} and expected {expected}"

# Usage
test_string_sequence(5) # Passes the test suite
```