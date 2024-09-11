### Caesar Cipher
#### Encoding and Decoding a String by Shifting Characters

Here's a Python script that implements the `encode_shift` and `decode_shift` functions:
```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: String to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Encoded string
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s if ch.isalpha()])

# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

Note that the `ord` function gives the ASCII value of a character, and `chr` gives the character represented by a specific ASCII value. The Caesar cipher works by shifting each letter by a certain number of positions down the alphabet. To handle uppercase and lowercase letters, we use the `isalpha` method to filter out non-alphabetic characters. The `% 26` operation ensures that the shifted values wrap around the alphabet if necessary.