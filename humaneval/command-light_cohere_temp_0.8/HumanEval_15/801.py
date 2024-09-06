```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)} {n+1}"
    
def test_string_sequence(test_cases: []):
    for case in test_cases:
        assert string_sequence(case) == f"0 {case}{' ' * (case - 1)} {case+1}", "String sequence failed test"
    
# Test cases
test_string_sequence([0, 5])
```