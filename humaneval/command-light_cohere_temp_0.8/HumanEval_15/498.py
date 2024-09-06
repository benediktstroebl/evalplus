```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

def test_string_sequence():
    assert str(test_string_sequence(5)) == "0 5 4 3 2 1", " passes
```
This code defines a function 'string_sequence' that generates a sequence of numbers in a string format starting from 0 up to the given 'n'. It also has a test function 'test_string_sequence' to check if the output of the function 'string_sequence' with the argument 'n' is equal to the expected output.