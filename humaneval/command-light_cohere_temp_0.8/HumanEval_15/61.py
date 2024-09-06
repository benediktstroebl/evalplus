```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_cases: list) -> None:
    for tc in test_cases:
        assert len(string_sequence(tc)) == (tc+1) * 2
        assert string_sequence("") == '0'
        assert string_sequence(0) == '0'
        assert string_sequence(10) == '9' '10 9 8 7 6 5 4 3 2 1'
        assert string_sequence(15) == '14 13 12 11 10 9 8 7 6 5 4 3 2 1'
```