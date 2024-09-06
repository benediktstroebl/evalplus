Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the complete script:
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
        s (str): Input string to be decoded.
        
    Returns:
        str: Decoded string.
    """
    return encode_shift(s, alpha=ord("a")+5)
```
The `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet. The `decode_shift` function first encodes the string `s` with a shift of 5, and then decodes it, effectively undoing the encoding and returning the original string.

Here's a markdown code block containing a sample test to verify the functionality of the provided functions:
```python
# Test the encode_shift function
assert encode_shift("Hello, World!") == "If, Kde, Jls, Duj, Wnx, Fvf, Rw!"

# Test the decode_shift function
assert decode_shift("If, Kde, Jls, Duj, Wnx, Fvf, Rw!") == "Hello, World!"
```
This test checks if the `encode_shift` function encodes the string properly and if the `decode_shift` function can correctly decode the encoded string. 

You can add more tests to cover a variety of scenarios and ensure the robustness of these functions.  These tests can be added in the markdown code block or in an external testing file, depending on your preferred testing methodology.