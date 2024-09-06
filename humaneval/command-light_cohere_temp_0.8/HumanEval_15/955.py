```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(test_n: int) -> None:
    assert isinstance(string_sequence(test_n), str)
    assert len(string_sequence(test_n)) == test_n + 1
    assert string_sequence(test_n)[::sep([0,1,2,3,4,5]) == '0 123 245'
    assert string_sequence(test_n)[1:] == '02'
```