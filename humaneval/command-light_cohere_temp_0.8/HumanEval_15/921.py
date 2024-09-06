```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence(test_cases):
    assert len(test_cases) == 0 or test_cases[0] == 0
    assert test_string_sequence(test_cases[0]) == "0" * (test_cases[0] +1)
    for n in range(1, 10):
        assert test_string_sequence(n) == f"0 {n}" * (n+1)
    return test_string_sequence(10)
```