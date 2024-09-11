### Shift Encoder and Decoder
#### Problem Description

The following Python script encodes and decodes a given string by shifting every character by 5 positions in the alphabet.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


# Example usage:
if __name__ == "__main__":
    input_str = "Hello, World!"
    encoded_str = encode_shift(input_str)
    print(f"Encoded String: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded String: {decoded_str}")
```

This script uses the `ord` function to get the ASCII value of each character and the `chr` function to convert ASCII value back to character. The `isalpha` method is used to check if a character is a letter before applying the shift operation. The result is converted to lowercase to maintain consistency.