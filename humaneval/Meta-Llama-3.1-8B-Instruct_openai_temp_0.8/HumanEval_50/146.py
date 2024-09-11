```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string is lowercase and does not contain any digits or special characters.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string is encoded with encode_shift function and only contains lowercase letters.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

In this code:

- The `encode_shift` function encodes the input string by shifting every lowercase letter by 5 positions in the alphabet.
- The `decode_shift` function decodes the input string by shifting every lowercase letter by -5 positions in the alphabet.
- The example usage at the end demonstrates how to use these functions with a sample string.