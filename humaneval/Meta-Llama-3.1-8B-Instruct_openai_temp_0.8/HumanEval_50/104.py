```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    In case the input string contains characters not in the alphabet, 
    they are left unchanged in the encoded string.
    
    Parameters:
    s (str): The string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    result = ""
    for ch in s:
        if ch.isalpha():
            ascii_offset = ord("a") if ch.islower() else ord("A")
            result += chr(((ord(ch) - ascii_offset + 5) % 26) + ascii_offset)
        else:
            result += ch
    return result


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    In case the input string contains characters not in the alphabet, 
    they are left unchanged in the decoded string.
    
    Parameters:
    s (str): The string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return encode_shift(s)


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_shift` and `decode_shift` functions according to the problem statement and includes an example usage section at the end to demonstrate their functionality. It handles both lowercase and uppercase letters while encoding and decoding the string, and leaves non-alphabet characters unchanged in both processes.