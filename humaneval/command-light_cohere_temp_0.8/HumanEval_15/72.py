```python
def string_sequence(n: int) -> str:
    return f" {0:02}".format(n)
    # tests
    assert isinstance(string_sequence(0), str), "Error: 0 not returned a string"
    assert isinstance(string_sequence(5), str), "Error: 5 not returned a string"
```