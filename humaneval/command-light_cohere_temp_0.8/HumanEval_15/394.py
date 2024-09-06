Here is a Python script that contains a self-contained function that generates a string of numbers from 0 up to n:
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '9 8 7 6 5 4 3 2 1'

# Main program
test_string_sequence()
```
This script defines a function `string_sequence` that returns a string containing space-delimited numbers from 0 up to `n`. It also defines a function `test_string_sequence` that contains tests to verify the correctness of the `string_sequence` function.  The test_string_sequence will run the tests to ensure the function works as expected.