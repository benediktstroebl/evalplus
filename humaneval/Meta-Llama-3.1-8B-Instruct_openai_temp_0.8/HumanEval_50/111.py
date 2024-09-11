```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script correctly implements the Caesar cipher by shifting every alphabetic character by 5 positions in the alphabet. Non-alphabetic characters are left unchanged. The `if ch.isalpha()` condition is used to handle both lowercase and uppercase letters. The `chr` and `ord` functions are used to convert between ASCII characters and their corresponding Unicode code points. The `% 26` operation ensures that the shifted characters wrap around the alphabet if necessary.