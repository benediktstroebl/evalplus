Here is a Python script that contains a self-contained function that returns a string containing space-delimited numbers from 0 up to n, with corresponding tests:
```python
import unittest
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return ' '.joinmap(str, range(n))
class TestStringSequence:
    unittest.testcase()
def test_string_sequence(self):
        self.assertEqual(string_sequence(0))
        self.assertEqual(string_sequence(5))
        self.assertEqual(string_sequence(10))
        self.assertEqual(string_sequence(0)) > '0'
        self.assertEqual(string_sequence(5)) > '0 1 2 3 4 5'
        self.assertEqual(string_sequence(10)) > '0 9 8 7 6 5'
if __name__ == "__main__":
    unittest.test()
```

This script defines a function `string_sequence` that returns a string containing space-delimited numbers from 0 up to n. The `TestStringSequence` class is used to run tests on the `string_sequence` function.  The script also imports the unittest module and defines a test function `test_string_sequence` that calls the string_sequence function with different input values and compares the output against the expected strings.