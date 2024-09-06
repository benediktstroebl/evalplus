```python
def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))
```

This approach uses the `zip` function to pair the corresponding characters of both strings, and then converts each pair to integers for XOR operation using the `^` exponentiation operator. The result is converted back to a character and joined together to form the final XORed string.

The tests could be performed within the function using Python's `unittest` module like so:
```python
import unittest

class TestStringXOR(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
    def test_empty_strings(self):
        self.assertEqual(string_xor('', '110'), '110')
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            string_xor('01', '11')
if __name__ == '__main__':
    unittest.main()
```