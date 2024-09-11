```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character to its corresponding ASCII value, 
    adding 5 and adjusting for the shift (wrapping around to the beginning of the alphabet if necessary), 
    then converting the result back to a character.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by first converting each character to its corresponding ASCII value, 
    subtracting 5 and adjusting for the shift (wrapping around to the end of the alphabet if necessary), 
    then converting the result back to a character.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
test_string = "Hello, World!"
encoded_string = encode_shift(test_string)
decoded_string = decode_shift(encoded_string)

print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

This script first defines the `encode_shift` and `decode_shift` functions as per the problem statement. It then provides example usage of these functions by encoding and decoding the string "Hello, World!". The encoded and decoded strings are printed to the console for verification.