Here's the Python script with a self-contained function that returns a string containing space-delimited numbers starting from 0 up to the input n:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space separated numbers starting from 0 to n inclusive"""
    return ' '.join([str(i) for i in range(n)])

def test_string_sequence():
    assert string_sequence(0) == '0', "Should return 0"
    assert string_sequence(1) == '1', "Should return 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should return 0 5"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0', "Should return 0 to 10"

# Call the function with test_string_sequence() to run the tests
```