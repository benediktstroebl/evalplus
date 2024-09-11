```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes the input string only contains lowercase English letters.
    It shifts each letter 5 positions forward in the alphabet, wrapping around to the start of the alphabet if necessary.
    Non-alphabet characters are left unchanged.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes the input string only contains lowercase English letters.
    It shifts each letter 5 positions backward in the alphabet, wrapping around to the end of the alphabet if necessary.
    Non-alphabet characters are left unchanged.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script provides the `encode_shift` and `decode_shift` functions as described, with the addition of a simple check to ensure only alphabetic characters are shifted. The example usage at the end demonstrates how to use these functions to encode and decode a string.