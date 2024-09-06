```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n
    
def test_string_sequence(test_case: str) -> None:
    assert isinstance(test_case, str), f"Input must be a string, got {type(test_case)}"
    assert len(test_case) == 1, f"Input must be a single integer, got {len(test_case)}"
    assert test_case == int(test_case) <= 10, f"Input must be a number between 0 and 10, got {test_case}"
    assert str(test_case) == string_sequence(int(test_case)), f"Failed Test: {test_case}"
    return None
```