```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr((ord(ch) - ord("a") + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr((ord(ch) - ord("a") - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


# Testing the functions
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

In this code block:

*   The `encode_shift` function encodes a given string by shifting each letter by 5 places in the alphabet. It uses the ASCII values of the characters and applies the Caesar Cipher algorithm. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value.
*   The `decode_shift` function decodes a string that has been encoded using the `encode_shift` function. It works in a similar way but shifts the characters back by 5 places in the alphabet.
*   In the testing section, we demonstrate how to use these functions by encoding and decoding a string. The original string, encoded string, and decoded string are printed to the console for verification.