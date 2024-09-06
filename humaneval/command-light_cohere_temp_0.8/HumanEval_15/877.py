Here is a self-contained Python script that defines and exercises the given function:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}" 

def test_string_sequence():
    """Test cases for the string_sequence function"""
    assert string_sequence(0) == "0", "Test case 0 failed"
    assert string_sequence(1) == "1", "Test case 1 failed"
    assert string_sequence(2) == "01", "Test case 2 failed"
    assert string_sequence(3) == "012", "Test case 3 failed"
    assert string_sequence(4) == "0104", "Test case 4 failed"
    assert string_sequence(5) == "0105", "Test case 5 failed"
    assert string_sequence(6) == "01106", "Test case 6 failed"
    assert string_sequence(7) == "01111", "Test case 7 failed"
    assert string_sequence(8) == "0217", "Test case 8 failed"

# Call the test suite
test_string_sequence()
```
The provided code defines a function test_string_sequence which contains a set of test cases to verify the functionality of the string_sequence function. The test_string_sequence function then runs these tests to ensure the correctness of the string_sequence function.