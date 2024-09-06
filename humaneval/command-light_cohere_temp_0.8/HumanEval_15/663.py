```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_num: int) -> None:
    assert len(string_sequence(test_num)) == test_num + 1
    assert string_sequence(test_num) == f"0 {test_num}" * (test_num + 1)
```