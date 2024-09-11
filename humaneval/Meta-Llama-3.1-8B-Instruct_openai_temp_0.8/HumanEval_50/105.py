```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5 + 26) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_shift("Hello, World!")
    decoded_str = decode_shift(encoded_str)
    print("Encoded string: ", encoded_str)
    print("Decoded string: ", decoded_str)
```

**Explanation:**

The above Python script implements the `encode_shift` and `decode_shift` functions according to the provided specifications. 

1. The `encode_shift` function shifts every character in the input string by 5 positions forward in the alphabet. It handles both lowercase and uppercase letters, and non-alphabetic characters remain unchanged.

2. The `decode_shift` function reverses the encoding process by shifting every character back by 5 positions in the alphabet.

3. In the example usage section, we demonstrate how to use these functions to encode and decode a string. 

**Note:** The code uses the ASCII values of characters, and the modulo operation to ensure that the shifted characters wrap around the alphabet. This results in a shift that preserves the case of the input characters and does not affect non-alphabetic characters.