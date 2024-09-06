```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..." * (n+1)

# Test case 1: Validate function with expected output
def test_string_sequence(test_n: int) -> None:
    assert string_sequence(test_n) == f"0 {test_n}..."* ({test_n+1})
    return 

# Test case 2: Validate with edge case
test_string_sequence(0)
```