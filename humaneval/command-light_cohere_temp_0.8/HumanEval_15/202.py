```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}{' ' * (n-1)}"

def test_string_sequence():
    """Function to test the string_sequence function."""
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(6) == '0 1 2 3 4 5'
    assert string_sequence(10) == "00010"
    assert string_sequence(123) == "00123"
``` 
This code defines a function `string_sequence` that returns a string containing space-separated numbers from 0 to n, inclusive. this function is tested a test function `test_string_sequence` which contains a collection of assertions to test the correctness of the `string_sequence` function with different inputs. 

This code is self-contained and can be used directly with the arguments provided to test the correctness of the string_sequence function.