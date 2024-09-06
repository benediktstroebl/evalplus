```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(test_n: int) -> None:
    assert len(string_sequence(test_n)) == test_n + 1
    assert string_sequence(test_n) == f"0 {test_n}" * (test_n+1)
    return

# Driver code to test the above function
test_sequence(6)
```