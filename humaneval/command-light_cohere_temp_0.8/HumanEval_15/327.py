```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test case for the above function:
def test():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == ' 02'
    assert string_sequence(3) == ' 0123'
    assert string_sequence(4) == '024'
    assert string_sequence(5) == '012345'

if __name__ == "__main__":
    test()
```