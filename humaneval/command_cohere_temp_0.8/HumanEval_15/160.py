```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

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

In the above code, the `string_sequence()` function uses the `range()` and `str()` functions to generate a sequence of numbers from 0 to `n` (inclusive) and converts them to a string formatted with spaces between the numbers. 

The `test_zero` and `test_five` functions test the `string_sequence()` function with respective to examples provided in the prompt. 

Finally, running the tests is done using `unittest.main()` in the script, which executes the test cases when the script is run directly. 

This solution should help you simulate and solve the problem within a Python environment.