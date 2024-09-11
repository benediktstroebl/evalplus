```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded
    
    Returns:
    str: Encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded
    
    Returns:
    str: Decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script includes both the `encode_shift` and `decode_shift` functions. The `encode_shift` function shifts every alphabetic character in the input string by 5 places to the right in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function does the reverse, shifting every alphabetic character by 5 places to the left in the alphabet.

The `if ch.isalpha()` condition in both functions is used to ignore non-alphabetic characters in the input string, so they do not affect the encoding or decoding process.

The example usage at the end of the script demonstrates how to use these functions with an example string.