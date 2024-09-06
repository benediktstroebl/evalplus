```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test case:
def test():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == '12'
    assert string_sequence(3) == '123'
    assert string_sequence(4) == '1234'
    assert string_sequence(5) == '12345'
    assert string_sequence(6) == 'lime'
    
# Run the above test case 
test()
```