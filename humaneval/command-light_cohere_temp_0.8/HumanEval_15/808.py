```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}"
    
def test_string_sequence():
    """Function to test the string_sequence function"""
    assert string_sequence(0) == '0', "String sequence failed for n=0"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence failed for n=5"
test_string_sequence()
```