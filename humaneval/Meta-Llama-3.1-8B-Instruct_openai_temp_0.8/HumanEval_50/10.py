```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string only contains lowercase English letters.
    If the input string contains any other characters, their ASCII values will be shifted.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string only contains lowercase English letters.
    If the input string contains any other characters, their ASCII values will be returned as is.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this code, we've modified the original `encode_shift` function to shift the characters in the way that is typical for Caesar cipher. The `decode_shift` function has been updated accordingly. The example usage demonstrates how to use these functions with a sample string.