```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n))

# Test the function
def test_string_sequence(test_num: int) -> None:
    assert string_sequence(test_num) == "".join(str(i) for i in range(test_num))
    return
test_string_sequence(10)
```