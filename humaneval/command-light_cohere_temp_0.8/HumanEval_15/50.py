```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

def test_sequence(test_case: int) -> None:
    assert string_sequence(test_case) == test_case(n)
    return None

# Example test cases
test_sequence(0)
test_sequence(1)
test_sequence(5)  # Passes
test_sequence(10) # Raises ValueError: Out of range: test_sequence(10) : {error}: unexpected EOF while scanning string literal
```