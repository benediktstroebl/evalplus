### Shift Encoder Decoder
#### Problem Description
Encode and decode a string by shifting every character by 5 in the alphabet.

#### Solution
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5 + 26) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])

# Example usage:
original_string = "Hello, World!"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print("Original String:", original_string)
print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
```
This solution uses the Caesar cipher algorithm to shift characters in the alphabet by a fixed number of positions. The `encode_shift` function shifts characters to the right by 5 positions, while the `decode_shift` function shifts them back to the left by 5 positions. Note that this solution only works for lowercase letters and ignores non-alphabet characters.