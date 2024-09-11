```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
    s (str): Input string

    Returns:
    str: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
    s (str): Encoded string

    Returns:
    str: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
input_str = "Hello World!"
encoded_str = encode_shift(input_str)
decoded_str = decode_shift(encoded_str)

print(f"Input: {input_str}")
print(f"Encoded: {encoded_str}")
print(f"Decoded: {decoded_str}")
```

This script uses the `ord` function to get the ASCII value of each character and then performs the required operations to shift the characters by 5 places in the alphabet. The `chr` function is used to get the character represented by the ASCII value. The `isalpha` function is used to check if a character is a letter. The script also converts the input string to lowercase before processing it, as the shift operation is case-insensitive.