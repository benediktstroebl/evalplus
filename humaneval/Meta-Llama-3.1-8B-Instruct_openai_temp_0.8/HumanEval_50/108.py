```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function shifts all lowercase letters by 5 positions in the alphabet.
    Characters that are not letters are ignored.
    
    Parameters:
    s (str): input string to be encoded.
    
    Returns:
    str: encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s if ch.isalpha() and ch.islower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function shifts all lowercase letters by 5 positions back in the alphabet.
    Characters that are not letters are ignored.
    
    Parameters:
    s (str): input string to be decoded.
    
    Returns:
    str: decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5 + 26) % 26 + ord("a")) for ch in s if ch.isalpha() and ch.islower()])


# Example usage:
input_str = "hello"
encoded_str = encode_shift(input_str)
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every character in the input string by 5 positions in the alphabet, while the `decode_shift` function shifts the characters back by 5 positions. The script also includes an example usage of these functions. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `isalpha` and `islower` methods are used to check if a character is a letter and if it is lowercase, respectively.