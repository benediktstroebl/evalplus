```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}..."[n+3].

def test_string_sequence(test_cases): 
    """Test string sequence function with different input values"""
    for n in test_cases:
        actual = string_sequence(n)
        expected = "".join()` + (" "*(n//3)) + str(n%3) + " ")
        assert actual == expected
```