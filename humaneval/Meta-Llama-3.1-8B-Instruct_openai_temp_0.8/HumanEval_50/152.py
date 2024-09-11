```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
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
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    result = ""
    for ch in s:
        if ch.isalpha():
            ascii_offset = ord("a") if ch.islower() else ord("A")
            result += chr(((ord(ch) - ascii_offset - 5) % 26) + ascii_offset)
        else:
            result += ch
    return result


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script defines the `encode_shift` function to shift each character in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function performs the reverse operation to decode the string. The example usage demonstrates how to use these functions with a sample string.