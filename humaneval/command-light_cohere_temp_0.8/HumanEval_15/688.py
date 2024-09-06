```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test cases
test_sequence = [
    deftest=lambda: assert str(test_sequence(42)) == '420 ', "Test 42 failed"
    deftest2=lambda: assert str(test_sequence(0)) == '0 ', "Test 0 failed"
    deftest3=lambda: assert str(test_sequence(1)) == '1 ', "Test 1 failed"
    deftest4=lambda: assert str(test_sequence(10)) == '100010 ', "Test 10 failed"
]
test_sequence()
```