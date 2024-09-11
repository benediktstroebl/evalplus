```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print("Original string:", original_string)
    print("Encoded string:", encoded_string)
    print("Decoded string:", decoded_string)
```

Note: This script uses the fact that the ASCII values for lowercase English letters 'a' through 'z' are consecutive, from 97 to 122. The expression `(ord(ch) - ord("a"))` calculates the position of a character in the alphabet (0 for 'a', 1 for 'b', and so on). The expression `((ord(ch) - ord("a") + 5) % 26)` shifts this position by 5 spaces, and the `chr` function converts it back to a character. The `% 26` operation ensures that if the shift would move the character outside the alphabet (e.g., from 'z' to 'z + 5'), it wraps around to the beginning of the alphabet.

The `if ch.isalpha()` condition in both functions filters out non-alphabetic characters, which would otherwise cause TypeError when trying to calculate their position in the alphabet.