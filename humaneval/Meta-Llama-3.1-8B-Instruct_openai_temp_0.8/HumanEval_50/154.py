```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): input string to be encoded
    
    Returns:
    str: encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): input string to be decoded
    
    Returns:
    str: decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and shifts every alphabetic character by 5 positions in the alphabet, wrapping around the alphabet if necessary. The `decode_shift` function does the reverse, shifting every character back by 5 positions.

The script also includes an example usage at the end to demonstrate how to use these functions.

Note that this script only shifts alphabetic characters and leaves non-alphabetic characters (such as punctuation and spaces) unchanged. Also, the functions are case-insensitive, so they treat 'a' and 'A' as the same character. If you want to preserve the case of the original string, you can modify the functions accordingly.