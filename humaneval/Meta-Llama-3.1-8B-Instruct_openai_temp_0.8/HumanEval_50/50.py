```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Shifts lowercase letters and keeps uppercase letters unchanged.
    
    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s])

# Example usage:
if __name__ == "__main__":
    encoded_string = encode_shift("Hello, World!")
    print("Encoded string:", encoded_string)
    decoded_string = decode_shift(encoded_string)
    print("Decoded string:", decoded_string)
```

This script defines the `encode_shift` and `decode_shift` functions as described. The `encode_shift` function shifts every lowercase letter by 5 positions in the alphabet, and leaves other characters unchanged. The `decode_shift` function reverses this process to decode the string.

The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `isalpha` function is used to check if a character is a letter.

In the example usage section, the script encodes the string "Hello, World!" using the `encode_shift` function, prints the encoded string, decodes it using the `decode_shift` function, and prints the decoded string.