Here is a self-contained Python script that defines and implements the string_sequence function as required:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 2 3 4 5..."format(n)

# Test the function with n = 0
test_string_sequence_0()
def test_string_sequence_0():
    assert string_sequence(0) == '0'

# Test the function with n = 5
test_string_sequence_5()
def test_string_sequence_5():
    assert string_sequence(5) == '0 1 2 3 4 5'

# Run the above tests
if __name__ == "__main__":
    unittest.test()

```
This script defines a function called string_sequence that returns a string containing space-delimited numbers starting from 0 up to n inclusive. The test_string_sequence_0 function tests if the string_sequence function returns '0' when passed n=0, and test_string_sequence_5 tests if the function returns the correct sequence of numbers when passed n=5. The script then runs the test using the unittest.run module.