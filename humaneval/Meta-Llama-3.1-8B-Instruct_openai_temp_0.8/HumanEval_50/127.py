```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    :param s: Input string
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: Encoded string
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded = encode_shift(original_string)
    decoded = decode_shift(encoded)
    
    print(f"Original: {original_string}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
```

In this script, the `encode_shift` and `decode_shift` functions are implemented as described. These functions use the ASCII values of characters to shift them by 5 places in the alphabet. The modulo operation is used to handle characters that are shifted beyond 'z' or 'Z'.

The `isalpha()` method is used to check if a character is a letter before attempting to shift it. This prevents attempts to shift non-letter characters, which would result in incorrect shifts.

The example usage at the end demonstrates how to use these functions to encode and decode a string. The `if __name__ == "__main__":` block is used to ensure that the example usage code only runs when the script is run directly (not when it is imported as a module).