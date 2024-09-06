```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n-1) + "}"

def test_string_sequence():
    """Test case function to check the correctness of string_sequence function"""
    assert string_sequence(0) == '0', "First test failed"
    assert string_sequence(1) == '1', "Second test failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Third test failed"
    assert string_sequence(10) == "00000", "Fourth test failed"
    
# main function to call test cases
test_string_sequence()
``` 
This script defines a function `string_sequence` that returns a string containing space-separated numbers from 0 up to the given `n`. The function is then tested with various input values using the `test_string_sequence` function, which checks the correctness of the `string_sequence` function.