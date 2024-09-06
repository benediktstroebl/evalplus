```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

def test_sequence(test_str: str) -> None:
    """Test string for the function"""
    assert len(test_str.contains('0'),'sequences do not match'
    assert test_str.contains('1'),'First number is 0.'
    assert test_str.contains('5','Last number is 5'),'Last number is not 5'
    assert test_str.contains('6'),'First number is 0 but after 3 numbers there is a 4.'

test_sequence("Test string")
```