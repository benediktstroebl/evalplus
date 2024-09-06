```python
def string_sequence(n: int) -> str:
    return f"0 {n} " * (n + 1)

# test suite
def test_string_sequence():
    assert string_sequence(0) == '0', "String not starts with 0"
    assert string_sequence(1) == '1', "String not has 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "String not has 5 numbers"
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1', "String doesn't have 10 numbers"

if __name__ == "__main__":
    test_string_sequence()
```