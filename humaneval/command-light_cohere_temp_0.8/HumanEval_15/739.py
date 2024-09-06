```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}"*n 

def test_string_sequence(test_cases: list[int]) -> None:
    for case in test_cases: 
        assert str(test_string_sequence(case)) == f"0 {case}*", end='if'
        return None 

# Example usage 
test_string_sequence([0, 5])
```