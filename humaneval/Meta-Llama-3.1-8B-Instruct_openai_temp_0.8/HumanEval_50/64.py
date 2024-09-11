### Shift Encoder and Decoder

The following Python script defines two functions, `encode_shift` and `decode_shift`, to encode and decode strings using a Caesar cipher with a shift of 5.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded
    
    Returns:
    str: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded
    
    Returns:
    str: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script first converts the input string to lowercase to simplify the encoding and decoding process. It then applies the Caesar cipher shift to each letter in the string, wrapping around the alphabet if necessary. Non-alphabetic characters are left unchanged. The `decode_shift` function is the inverse of `encode_shift`, simply subtracting 5 from each letter's shift instead of adding. Finally, the script demonstrates how to use these functions with an example string.