```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

#Test cases
test_seq = [
    assert string_sequence(0) == '0', "Test case 0 failed"
    assert string_sequence(1) == '1', "Test case 1 failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Test case 5 failed"
    assert string_sequence(10) == "000010", "Test case 10 failed"
]
```