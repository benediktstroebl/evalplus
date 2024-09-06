```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}" * (n + 1)

def test_string_sequence(test_n: int) -> None:
    assert str(test_string_sequence(test_n)) == f"0 {test_n}" * (test_n + 1), "Test failed"

# Test the function with different values of n
test_string_sequence(0)
test_string_sequence(5)
test_string_sequence(9)
test_string_sequence(15)
```