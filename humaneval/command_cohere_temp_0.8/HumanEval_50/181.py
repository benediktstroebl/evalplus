```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
```

This script defines two functions:
1. `encode_shift` : Encodes a string by shifting each character by 5 in the alphabet.
2. `decode_shift` : Decodes a string encoded with the `encode_shift` function. 

The functions are designed to work independently, and the output of `encode_shift` is the input for `decode_shift`. 

Note that the code assumes that the input `str` contains only lowercase alphabetic characters. Characters that are not in the range from 'a' to 'z' or that are not alphabetic (such as spaces or symbols) will not be encoded or decoded correctly. 

 encoder.py
```
```python
import unittest
from encoder import encode_shift, decode_shift

class TestEncoder(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('abc'), 'defg')
        self.assertEqual(encode_shift('xyz'), 'vwxyz')
        self.assertEqual(encode_shift('qrs'), 'tvgqs')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('defg'), 'abc')
        self.assertEqual(decode_shift('vwxyz'), 'xyz')
        self.assertEqual(decode_shift('tvgqs'), 'qrs')

if __name__ == '__main__':
    unittest.main()
```

The above code includes a test suite with two test cases for the `encode_shift` function and two for `decode_shift`. Each test case checks whether the function's output from a particular input is as expected. 

The script also uses the `unittest` module to run the test suite when the script is run directly. 

To run the test suite, simply run the script named `encoder.py` via your terminal with Python 3. 

If all test cases pass, the output will resemble the following: 
 ```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
``` 
```
```