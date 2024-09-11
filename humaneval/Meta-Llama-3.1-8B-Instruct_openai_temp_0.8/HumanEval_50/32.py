### Caesar Cipher Decoder

#### Problem Description

Implement a Python script that encodes and decodes a given string by shifting every character by 5 places in the alphabet.

#### Code
```python
def encode_shift(s: str) -> str:
    """
    Encodes a string by shifting every character by 5 places in the alphabet.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str) -> str:
    """
    Decodes a string that was encoded using the encode_shift function.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

#### Explanation

This script uses the Caesar cipher technique to encode and decode strings. The `encode_shift` function shifts every alphabet character in the input string by 5 places to the right, and the `decode_shift` function shifts every alphabet character by 5 places to the left. Non-alphabet characters are left unchanged.

The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `% 26` operation ensures that the shift wraps around the alphabet.

The `isalpha` method is used to check if a character is a letter, and the `lower` method is used to convert the input string to lowercase to handle both uppercase and lowercase letters.