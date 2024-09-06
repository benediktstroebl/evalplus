```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_cases): 
    for test in test_cases:
        assert str(test_sequence(test)) == test
```