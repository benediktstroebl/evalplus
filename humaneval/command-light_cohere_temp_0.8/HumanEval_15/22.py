```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} 000"
    
def test_sequence(test_cases: []):
    for case in test_cases:
        assert str(test_sequence(case)) == f"0 {case} 000"

# Test the function with some test cases
test_sequence([5])
```