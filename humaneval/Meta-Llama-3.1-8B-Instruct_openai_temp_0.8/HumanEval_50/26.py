```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    The function converts each character to its corresponding ASCII value, adds 5, 
    takes the modulus of 26 to wrap around the alphabet, and then converts back to 
    a character. This process is repeated for each character in the input string.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    The function works by shifting each character back by 5 places in the alphabet.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
input_string = "hello"
encoded_string = encode_shift(input_string)
decoded_string = decode_shift(encoded_string)

print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

This script defines the `encode_shift` and `decode_shift` functions and includes example usage to demonstrate their functionality. The `encode_shift` function shifts each character in the input string by 5 places in the alphabet, while the `decode_shift` function reverses this process to obtain the original string. The example usage shows how to encode and decode a string using these functions.