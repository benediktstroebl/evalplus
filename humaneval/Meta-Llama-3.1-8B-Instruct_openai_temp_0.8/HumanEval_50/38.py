### Shift Encoder and Decoder
#### Python Implementation

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s if ch.isalpha()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) for ch in s if ch.isalpha()]).lower()


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script includes two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabetic character in the input string by 5 positions in the alphabet, while the `decode_shift` function reverses this process to retrieve the original string. The script also includes a basic example usage at the end. The `isalpha()` and `lower()` methods are used to handle both lowercase and uppercase characters, as well as non-alphabetic characters in the input string.