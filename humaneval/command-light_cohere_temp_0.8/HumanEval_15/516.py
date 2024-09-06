Here is a Python script that contains a self-contained function that returns a string containing space-delimited numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n)])

# Test the function
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(100) == '0 99 98 97 96 95 90 89 80 71 68'

test_string_sequence()
```