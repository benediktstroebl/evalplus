```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n 

# Test the function
def test_string_sequence(test_case: str) -> None:
    assert test_case == test_string_sequence(int(test_case)),
    return 

# Test 0
test_string_sequence(0)
# Test 5
test_string_sequence(5)
```