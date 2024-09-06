Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block demonstrating the solution:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string encoded with encode_shift.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) >= 0 else ((ord(ch) - ord("a")) % 26)) or ord("a")) for ch in s])
```

The corresponding test cases in the markdown code block are:
```python
import unittest
from encode_shift import encode_shift, decode_shift

class TestEncodeShift(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift("Hello World!), &"), "Ijly mkdir Bn")
    def test_decode_shift(self):
        self.assertEqual(decode_shift("Ijly mkdir Bn"), "Hello World!), &")

if __name__ == '__main__':
    unittest.main()
```

The script defines two functions, `encode_shift` and `decode_shift`, that take an input string and shift each character by 5 in the alphabet to encode it and then decode it respectively. The `encode_shift` function is tested by checking if the encoded string is correct for the input string "Hello World!), &". The `decode_shift` function is tested by checking if the decoded string is correct for the encoded string "Ijly mkdir Bn". 

The test suite is run using `unittest.main()` when the script is executed directly. 

Please let me know if this solution satisfies the problem you presented! I'm here to clarify or further refine the response if needed.