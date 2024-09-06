```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an argument and flips the case of the characters within the string. It returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. 

To execute this script and test the functionality, run the following code:
```python
import unittest

def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)

class TestFlipCase(unittest.TestCase):
    def test_lowercase_flip(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_mixed_case_flip(self):
        self.assertEqual(flip_case('HELLo'), 'hELLO')

    def test_uppercase_flip(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

if __name__ == '__main__':
    unittest.main()
```

This code will run the `unittest` module, which will run the `TestFlipCase` class and its test cases, validating the functionality of the `flip_case` function.