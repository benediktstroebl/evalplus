```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
    s (str): Input string
    
    Returns:
    str: Encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
    s (str): Input string
    
    Returns:
    str: Decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script first defines two functions: `encode_shift` for encoding a string by shifting every character by 5 in the alphabet and `decode_shift` for decoding a string that was previously encoded with `encode_shift`. The `chr` function is used to get the character represented by a specific ASCII value, and the `ord` function is used to get the ASCII value of a character. The `isalpha` method is used to check if a character is a letter.

The `if __name__ == "__main__":` block is used to ensure that the example usage code only runs when the script is executed directly (not when it's imported as a module). In the example usage, we encode a string, print the original and encoded strings, decode the encoded string, and print the decoded string.