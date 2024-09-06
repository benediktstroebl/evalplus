```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_cases: list) -> None:
    assert string_sequence(test_cases[0]) == "0 0",
    assert string_sequence(test_cases[1]) == "0 1",
    assert string_sequence(test_cases[2]) == "0 2",
    assert string_sequence(test_cases[3]) == "0 3",
    assert string_sequence(test_cases[4]) == "0 4",
    assert string_sequence(test_cases[5]) == "0 5"
    
test_string_sequence([0, 5])
```