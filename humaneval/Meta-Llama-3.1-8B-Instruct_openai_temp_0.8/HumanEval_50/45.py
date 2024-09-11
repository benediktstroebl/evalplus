### Shift Encoder and Decoder Script
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function considers both lowercase and uppercase letters. 
    However, note that the casing of the original characters is preserved.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) * (ch.islower() or ch.isalpha())) + ord("a") if ch.isalpha() and ch.islower() else chr(((ord(ch) - ord("A")) % 26 + 5) * (ch.islower() or ch.isalpha())) + ord("A") if ch.isalpha() and ch.isupper() else ch for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function considers both lowercase and uppercase letters. 
    However, note that the casing of the original characters is preserved.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) * (ch.islower() or ch.isalpha())) + ord("a") if ch.isalpha() and ch.islower() else chr(((ord(ch) - ord("A")) % 26 + 5) * (ch.islower() or ch.isalpha())) + ord("A") if ch.isalpha() and ch.isupper() else ch for ch in s])

# Test the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script defines two functions, `encode_shift` and `decode_shift`, to shift every character in a string by 5 positions in the alphabet. The script also includes a test case to demonstrate the functionality of the functions.