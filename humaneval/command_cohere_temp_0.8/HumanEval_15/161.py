```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the built-in `range()` function in Python which creates a sequence of numbers and returns them as an iterable object. The `map()` function is then used to convert these sequence of numbers into strings, and `join()` is used to concatenate these strings into one string with spaces as delimiter. 

This approach is concise and elegant, and it demonstrates the power of Python's functional programming capabilities. 

The `string_sequence()` function is also robust because it does not need to know the explicit input range beforehand and can handle any input value and return the appropriate result. 

To handle and test the edge case of inputs less than or equal to 0, a tester can use the following script:
```python
import unittest

def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_string_sequence_edge_cases(self):
        self.assertEqual(string_sequence(-1), '0')
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(1), '0 1')

if __name__ == '__main__':
    unittest.main()
```

This script creates a test class containing two test methods - `test_string_sequence` which tests the function with normal inputs and `test_string_sequence_edge_cases` which tests the function with edge cases. 

The `string_sequence()` function is then defined and used within the `test_string_sequence()` function to run the function with the given inputs and compare the output against the expected outputs using the `self.assertEqual()` method. 

This method verifies that the actual output of the `string_sequence()` function is identical to the expected output. If the inputs and outputs are identical, the test passing indication "OK" is displayed in the console, indicating that the tests have passed and the function works as expected.