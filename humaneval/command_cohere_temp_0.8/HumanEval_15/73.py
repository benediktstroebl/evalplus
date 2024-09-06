```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

The `string_sequence` function uses the `range` and `map` functions to generate a list of numbers from 0 to `n` (inclusive), and then joins these numbers into a single string with spaces as the delimiter. The `test_string_sequence` function verifies that the `string_sequence` function behaves as expected for different values of `n`. The final test assertion ensures that the function is correct for a larger value of `n`. 

To run the test, you can add the following code before the final test assertion: 

```python
# Importing the unittest module is necessary to run the tests
import unittest

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

if __name__ == '__main__':
    unittest.main()
```

This will run the test and indicate if it fails. 

If you intend to pose more problems or provide extra details, please do so and I will do my best to assist you!