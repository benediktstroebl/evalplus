```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
import pytest

def test_string_sequence():
    """Test the string_sequence() function."""
    
    # Basic Test Cases:
    assert string_sequence(0) == '0'
    assert string_sequence(4) == '0 1 2 3 4'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

    # Edge Case:
    with pytest.raises(ValueError):
        string_sequence(-1)

    # Large Input:
    assert string_sequence(55) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55'
```

You can safely copy and paste this code into a Python environment or script to use the `string_sequence()` function as defined. 

To run the tests, you'd need to install the `pytest` library. Once installed, you can run the tests with the command `pytest -v` in the file containing this code. These tests will evaluate the correctness of the `string_sequence` function with various inputs and confirm its operationality. 

If you are interested in learning more about testing in Python, you can read about it in the Python Documentation at this [URL](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-tests). 

If you'd like to delve deeper into the subject of Python or Python functions, feel free to ask subsequent questions!