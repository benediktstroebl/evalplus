```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): input string to be encoded
    
    Returns:
    str: encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): encoded string to be decoded
    
    Returns:
    str: decoded string
    """
    return "".join([chr(((ord(ch) - (ord("a") + 5 - (ord(ch) - ord("a")) % 26)) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    input_string = "Hello, World!"
    encoded_string = encode_shift(input_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabetic character in the input string by 5 positions forward in the alphabet. The `decode_shift` function takes the encoded string and shifts every alphabetic character back by 5 positions. The functions use the modulo operator (`%`) to ensure the shifted characters wrap around the alphabet if necessary. Both functions only consider lowercase alphabetic characters (a-z). The example usage at the end demonstrates how to use these functions to encode and decode a string.