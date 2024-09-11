```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.
    
    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
        s (str): Input string to be decoded.
    
    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_shift` and `decode_shift` functions as specified. The `encode_shift` function shifts every alphabetical character in the input string by 5 positions in the alphabet, wrapping around the alphabet if necessary. The `decode_shift` function reverses the encoding process, shifting the characters back by 5 positions. The example usage in the `if __name__ == "__main__":` block demonstrates how to use these functions to encode and decode a string.