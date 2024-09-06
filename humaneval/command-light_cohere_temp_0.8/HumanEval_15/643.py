Here is a self-contained Python script that solves the problem of generating a sequence of numbers in a markdown code block:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}" 

def test_string_sequence():
    """Test the function with different values of n"""
    assert string_sequence(0) == "0", "Test failed: 0"
    assert string_sequence(1) == "1", "Test failed: 1"
    assert string_sequence(5) == "0 1 2 3 4 5", "Test failed: 5"
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1", "Test failed: 10"
```