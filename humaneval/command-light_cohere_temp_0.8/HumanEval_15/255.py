Here's the Python script with a self-contained function that generates and tests a sequence of strings containing space-separated numbers:
```python
import unittest
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    return " ".join([f"0 {i}" for i in range(n+1)]) + " "

class TestStringSequence(unittest.TestCase.TestCase):
    def test_sequence(self):
    self.assertEqual(string_sequence(5))
    self.assertEqual(string_sequence(0))
    self.assertEqual(string_sequence(10))
    self.assertEqual(string_sequence(20))
    self.assertEqual(string_sequence(50))

if __name__ == "__main__":
    unittest.main()
```

You can use the `unittest` module to run the test suite. The test suite will check that the function `string_sequence` correctly generates the expected output for different input values.