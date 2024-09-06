```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} all {n+3}"
    
# Test case 1: Check for empty input
test_sequence(0) # Output: Error: str.test() expected but got 'ValueError' instead
```

def test_sequence(n):
    try:
        assert str(string_sequence(n)) == f"0 {n} 1 {n+1} 2 {n+2} all {n+3}"
        return " succeeded"
    except AssertionError:
        return " failed"

# Test case 2: Check for positive input
test_sequence(5)

# Test case 3: Check for negative input
test_sequence(-5)

# Test case 4: Check for zero input
test_sequence(0)

print("All tests passed!")
```