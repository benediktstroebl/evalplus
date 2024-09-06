```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    """Test case function"""
    assert string_sequence(0) == "0", "Test case 0 failed: " + assert_fail"
    assert string_sequence(1) == "1", "Test case 1 failed: " + assert_fail
    assert string_sequence(5) == "0 1 2 3 4 5", "Test case 5 failed: " + assert_fail
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1", "Test case 10 failed: " + assert_fail

```
The above Python script provides a self-contained function `string_sequence` that calculates and returns a string containing space-separated numbers from 0 to n, inclusive. The `test_string_sequence` function passes a series of tests to ensure the correctness of the `string_sequence` function.