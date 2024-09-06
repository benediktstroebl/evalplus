```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert string_sequence(0) == '0', "Failed test case 0"
    assert string_sequence(1) == '1', "Failed test case 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Failed test case 5"
    assert string_sequence(10) == '0 10 10 10 10', "Failed test case 10"
    assert string_sequence(15) == '0 15 15 15 15', "Failed test case 15"
    assert string_sequence(50) == '0 50 50 50 50', "Failed test case 50"
```