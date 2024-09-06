```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}..."[n+3]

def test_string_sequence():
    """Test the function by passing different values and asserting the expected output"""
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "1"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 10 10 10"
    assert string_sequence(15) == "0 15 15 15"

    print("Tests passed!")

# Your code here.
```