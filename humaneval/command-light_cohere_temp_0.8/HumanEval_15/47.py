```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_case: int) -> None:
    assert isinstance(test_case, int)
    assert str(test_case) == '0' + str(test_case)
    assert string_sequence(test_case) == f"0 {test_case}"*((test_case+1))
    assert len(string_sequence(test_case)) == test_case+1
    return None # Returns None to indicate passing all tests
```