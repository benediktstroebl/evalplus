### Caesar Cipher Encoder and Decoder
#### Using Python

Here is a self-contained Python script that defines two functions, `encode_shift` and `decode_shift`, to implement the Caesar cipher for encoding and decoding strings.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 21) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes an input string and shifts every character by 5 in the alphabet. The `decode_shift` function takes a string encoded with `encode_shift` and shifts it back by 5 to get the original string. 

The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to convert an ASCII value back to a character. The `%` operator is used to wrap around the alphabet when shifting characters.

The example usage at the end of the script shows how to use these functions to encode and decode a string.