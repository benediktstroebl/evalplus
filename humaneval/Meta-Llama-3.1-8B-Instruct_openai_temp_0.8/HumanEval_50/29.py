### Caesar Cipher Encoder and Decoder
#### Python Script

```markdown
### Problem Statement

Implement a Caesar Cipher encoder and decoder in Python. The `encode_shift` function should shift every character in the input string by 5 positions in the alphabet. The `decode_shift` function should reverse this operation.

### Solution

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    The function uses the Caesar Cipher algorithm, shifting each character in the input string by 5 positions in the alphabet.
    Lowercase letters are shifted from 'a' to 'z', and the shift is performed using the modulo operator to wrap around the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function is the inverse of encode_shift. It decodes a string that was previously encoded using the encode_shift function.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
original_string = "Hello, World!"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

### Explanation

The `encode_shift` function works by subtracting the ASCII value of 'a' from each character, adding 5, taking the result modulo 26 to wrap around the alphabet, and then adding the ASCII value of 'a' back to get the encoded character. The `decode_shift` function performs the inverse operation to reverse the encoding process.

The `isalpha` method is used to check if each character is a letter before applying the encoding or decoding operation. Non-letter characters are left unchanged.

The example usage demonstrates how to use the `encode_shift` and `decode_shift` functions to encode and decode a string, and prints the original, encoded, and decoded strings for comparison.