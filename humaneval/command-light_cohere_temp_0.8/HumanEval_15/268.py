```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

def test_string_sequence(test_n: int) -> None:
    assert len(string_sequence(test_n)) == 3*test_n
    assert string_sequence(0) == '0\n'
    assert string_sequence(1) == '1\n'
    assert string_sequence(3) == '3\n3'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 10 10 10 10'
    return
test_string_sequence(5)
```