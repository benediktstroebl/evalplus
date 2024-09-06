```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == ' 02'
    assert string_sequence(3) == ' 0103'
    assert string_sequence(4) == ' 0404'
    assert string_sequence(5) == ' 05055'
    assert string_sequence(6) == ' 06'
    assert string_sequence(7) == ' 07'
    assert string_sequence(8) == ' 0800'
    assert string_sequence(9) == ' 09'
    assert string_sequence(10) == '00010'
```