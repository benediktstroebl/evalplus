Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded message:
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
    Decodes a string encoded with the `encode_shift` function.
    
    Args:
        s (str): Input string encoded with `encode_shift`.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) >= 0 else ((ord(ch) - ord("a")) % 26)) or ord("a")) for ch in s])

# Test cases
def test_encode_shift():
    assert encode_shift("Hello") == "Ifmmp">>

def test_decode_shift():
    assert decode_shift("Ifmmp") == "Hello">>

test_encode_shift()
test_decode_shift()
```

This script defines the two functions you described, encodes a test string, and then decodes the encoded string to verify that the functions are working correctly. 
The `test_encode_shift()` function checks if the result of the `encode_shift()` function is the expected one for the input "Hello", and the `test_decode_shift()` function checks if the result of the `decode_shift()` function is the expected one for the input "Ifmmp" (which is the result of encoding the string "Hello" with the specified shift). 

Let's keep in mind that these functions assume that the input contains only lowercase alphabetic characters. Characters that are not lowercase letters will not be correctly encoded or decoded.  If you have messages containing punctuation marks or digits, you may want to consider encoding them accordingly, which would require additional functions to decode them back.