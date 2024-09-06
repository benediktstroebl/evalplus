```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function
def test_string_sequence(test_cases):
    for _ in range(test_cases):
        assert string_sequence(_) == f"0 {_}".format()

# Test cases
test_cases = [0, 5]
test_string_sequence(test_cases)
```