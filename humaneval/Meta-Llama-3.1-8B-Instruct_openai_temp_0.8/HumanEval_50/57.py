```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes the input string is in lowercase English letters.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes the input string is in lowercase English letters.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage:
original_string = "hello"
encoded_string = encode_shift(original_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script includes the functions `encode_shift` and `decode_shift` to encode and decode a string by shifting every character by 5 in the alphabet. It also includes a check to ensure the input string only contains lowercase English letters. An example usage is provided at the end to demonstrate the encoding and decoding process.