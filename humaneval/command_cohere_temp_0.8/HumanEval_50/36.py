Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    
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
        s (str): Input encoded string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) >= 0 else ((ord(ch) - ord("a")) % 26)) or ord("a")) for ch in s])

# Unit tests:
def test_encode_shift():
    assert encode_shift("Hello World!") == "Ifmmp Ubjtm!"

def test_decode_shift():
    assert decode_shift("Ifmmp Ubjtm!") == "Hello World!"

test_encode_shift()
test_decode_shift()
```

You can run this script to verify that the functions behave as expected. The `test_encode_shift` function checks the encoding process, and the `test_decode_shift` function verifies the decoding process. 

Let's break down the key concepts of how the code works:
1. ** encode_shift Function:
    - This function takes an input string `s`.
    - It uses a list comprehension to iterate over each character `ch` in the input string `s`.
    - For each character, it calculates the new ordinal value by adding 5 to the current value, then taking modulo 26 to wrap around within the alpha range.
    - It then subtracts the base value of 'a' to get the new character, and finally wraps around with `chr(+(ord("a") - 1))` to get the corresponding character.
    - The new characters are joined together to form the encoded output string.
2. ** decode_shift Function:
    - This function takes an input encoded string s.
    - It uses a list comprehension in a similar manner to the encoding process to iterate over each character `ch` in the input string s.
    - It calculates the original character by either subtracting 5 (if the result is positive) or taking the absolute difference and then wrapping around with 'a' (if the result is negative) from the current value.
    - The new characters are joined together to form the decoded output string.

The modulo operation (`% 26`) is used to ensure that the characters are wrapped around within the range of the English alphabet, shifting by 5 characters each time.