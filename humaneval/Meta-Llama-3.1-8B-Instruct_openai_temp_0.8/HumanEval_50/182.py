```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Normally, 'a' has an ASCII value of 97. In the alphabet, 'a' has the ASCII value of 97 and 'z' has the value of 122.
    We use the formula (ord(ch) - ord('a') + shift) % 26 + ord('a') for shifting.
    For lower case characters only.
    
    Parameters:
    s (str): The string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Parameters:
    s (str): The string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Testing the functions
original_string = "hello world abc"
encoded_string = encode_shift(original_string)
print("Original string: ", original_string)
print("Encoded string: ", encoded_string)
print("Decoded string: ", decode_shift(encoded_string))
```

This script includes two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes a string and returns a new string where each character is shifted 5 positions forward in the alphabet. The `decode_shift` function takes a string that was encoded with `encode_shift` and returns the original string.

Note: Both functions handle only lowercase characters and there's a condition added to check if the character is an alphabet letter before applying the shift.