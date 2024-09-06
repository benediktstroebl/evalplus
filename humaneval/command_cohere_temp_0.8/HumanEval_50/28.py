Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "qrstuvwxyzabcdefghijklm"))
```
The `encode_shift` function takes a string s as input and returns an encoded version of the string. For every character in the string, it applies a shift of 5 in the alphabet. In other words, it computes the new character using the formula `(old_char - 97 + 5) % 26 + 97`, which shifts each character by 5 in the alphabet, and wraps around `abcdefghijklmnopqrstuvwxyz` accordingly. This encoded string is then returned as the output. 

The `decode_shift` function takes a string s as input and returns a decoded string. It uses the `translate` function to shift each character back to its original position using the translation table `str.maketrans("abcdefghijklmnopqrstuvwxyz", "qrstuvwxyzabcdefghijklm")`. 

This translation table reverses the shift applied in the `encode_shift` function, decoding the encoded string and returning the original string. 

This script includes self-contained functions that solve the problem statement and can be executed independently. 
```python
import unittest

class TestStringCoding(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift("Hello"), "khoor")
        self.assertEqual(encode_shift("World"), "lcawd")
        self.assertEqual(encode_shift("!),!".encode()), "8==&")

    def test_decode_shift(self):
        self.assertEqual(decode_shift("khoor"), "Hello")
        self.assertEqual(decode_shift("lcawd"), "World")
        self.assertEqual(decode_shift("8==&".encode()), "!),!")

if __name__ == '__main__':
    unittest.main()
```