```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

# Example usage:
original_str = "Hello, World!"
encoded_str = encode_shift(original_str)
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script will take a string, shift each letter by 5 positions forward, and then shift it back to get the original string. The script also lowercases the string first, since the shift function is designed for lowercase letters. 

Note: This script will treat uppercase letters as lowercase letters, and will not correctly shift them. If you want to correctly shift both lowercase and uppercase letters, you will need a more complex solution. 

The `isalpha()` function is used to filter out non-alphabetic characters from the string.