Here is a Python script that contains a self-contained function that generates a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{" + string_sequence(n-1) + "}"

def test_string_sequence():
    """Test the function with different values of n"""
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "1"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1"
    assert string_sequence(100) == "0 99 98 97 96 95 94 90 83 82 71 68 65"

# Call the function with a number of terms to generate
string_sequence(20)
```