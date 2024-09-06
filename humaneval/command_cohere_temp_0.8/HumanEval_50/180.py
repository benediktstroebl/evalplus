Here's a Python script with a self-contained function that solves the problem:
```python
#!, encode_shift, and decode_shift functions
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
#unittest
import unittest

class Test encode_shift(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_shift("hello"),"ifmmp">)
        self.assertEqual(encode_shift("abcd"),"bgcd")
        self.assertEqual(encode_shift("abcde"),"ckfg")
        self.assertEqual(encode_shift("abcdef"),"dlmhq")
    def test_edge(self):
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(encode_shift("abc"),"bgc")
        self.assertEqual(encode_shift("abcba"),"cklb")

class Test decode_shift(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(decode_shift("ifmmp"),"hello")
        self.assertEqual(decode_shift("bgcd"),"abcd")
        self.assertEqual(decode_shift("ckfg"),"abcde")
        self.assertEqual(decode_shift("dlmhq"),"abcdef")
    def test_edge(self):
        self.assertEqual(decode_shift(""), "")
        self.assertEqual(decode_shift("abc"),"abc")
        self.assertEqual(decode_shift("cklb"),"abcba")
if __name__ == '__main__':
    unittest.main()
```

This script defines the `encode_shift` and `decode_shift` functions and tests them using `unittest`. 

The `encode_shift` function shifts each character in the input string `s` by 5 in the alphabet. It returns the encoded string using these rules:
- `a` is encoded as `f`
- `b` is encoded as `g`
- `c` is encoded as `h`
- `d` is encoded as `i`
- `e` is encoded as `j`
The `decode_shift` function takes an encoded string from the `encode_shift` function and returns the decoded string using these rules:
- `f` is decoded as `a`
- `g` is decoded as `b`
- `h` is decoded as `c`
- `i` is decoded as `d`
- `j` is decoded as `e` 

The `Test encode_shift` and `Test decode_shift` classes test the functions with various inputs, including edge cases, to ensure they provide the expected outputs. 

Finally, the `unittest.main()` function runs the tests when the script is executed directly.  This thorough approach assists in verifying that the code operates as expected and addresses the problem statement effectively.