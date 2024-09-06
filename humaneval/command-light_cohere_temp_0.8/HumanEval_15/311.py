```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_string_sequence = """
def test_string_sequence(n):
    assert string_sequence(n) == f"0 {n}" * (n+1)
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 5 10 15 20'
test_string_sequence
"""
```