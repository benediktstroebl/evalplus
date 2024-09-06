```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    """Helper function to split the returning string into an array of spaces and numbers"""
    return ' '.joinmap(str, f"0 {n} {" + str_sequence(n-1) + "}")

def test_string_sequence():
    """Tests the string_sequence function with various inputs"""
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1'
    assert string_sequence(1) == '0 1'
    assert string_sequence(0) == '0'
    assert str_sequence(6) == '0  6'
    assert str_sequence(11) == '0  9 8 7'
    assert str_sequence(14) == '0  9 8 6 5 4 3 2 1'

if __name__ == "__main__":
    test_string_sequence()
```