```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
    print(f"Decoded string (lowercase): {decoded_string.lower()}")
```

This script solves the problem you described and provides an example usage. The `encode_shift` function shifts every lowercase letter in the input string by 5 positions in the alphabet and lowers the rest of the characters. The `decode_shift` function does the reverse operation to restore the original string. Both functions use the ASCII values of the characters to perform the shift.

Note that the `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `(ch - ord("a"))` expression is used to shift the lowercase letters to a range of 0-25, where 'a' corresponds to 0 and 'z' corresponds to 25, and then the result is added to 5 (or subtracted by 5 for decoding) and reduced modulo 26 to ensure the result is still within this range. The resulting value is then added to `ord("a")` to get the ASCII value of the shifted character.