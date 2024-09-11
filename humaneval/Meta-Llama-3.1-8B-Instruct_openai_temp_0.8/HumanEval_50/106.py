```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded
    
    Returns:
    str: The encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded
    
    Returns:
    str: The decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` to shift every character in a string by 5 places to the right in the alphabet, and `decode_shift` to shift every character back by 5 places to the left. The example usage at the end demonstrates how to encode and decode a string using these functions. 

Note: The `isalpha()` function checks if a character is a letter, and the `lower()` function converts the string to lowercase to simplify the encoding and decoding process. This ensures that the functions work correctly regardless of the case of the input string.