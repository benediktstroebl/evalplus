```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
import unittest

class TestStringSequence(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_five(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()
```

The `string_sequence` function uses the `range` and `map` functions to generate a list of numbers from 0 to `n` (inclusive), and then joins these numbers into a single string with spaces as the delimiter.

The test suite consists of two test cases:
- `test_zero`: Validates that the function returns '0' when `n` is set to 0.
- `test_five`: Verifies that the function produces the correct string for n = 5. 

The `unittest.main()` function is used to discover and run the tests. 

To execute the code from the command line, ensure that the Python script is the current working directory and run: 
`python test.py`