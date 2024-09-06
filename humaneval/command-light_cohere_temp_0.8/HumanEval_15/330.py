```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)
    pass

# Test case:
def test_string_sequence(test_case: str) -> None:
    assert len(test_case) == 1 + len(str(test_case))
    assert test_case == f"0 {test_case}1"*len(str(test_case))
    assert test_case == f"{0}{1}{2}..."*len(str(test_case))
    assert test_case == f"{0}{2}{3}..."*(len(str(test_case))-2)
    return None

# Example usage:
test_string_sequence("0")
```