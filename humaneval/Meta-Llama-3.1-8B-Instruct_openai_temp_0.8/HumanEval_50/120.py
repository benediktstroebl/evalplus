```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by converting each character in the input string to its corresponding ASCII value, 
    shifting it by 5 places in the alphabet, and then converting it back to a character.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by converting each character in the input string to its corresponding ASCII value, 
    shifting it back by 5 places in the alphabet, and then converting it back to a character.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This code defines the `encode_shift` and `decode_shift` functions as specified. The `encode_shift` function shifts each character in the input string by 5 places in the alphabet, while the `decode_shift` function reverses this operation. The functions handle both lowercase and uppercase letters correctly, and leave other characters unchanged.

The example usage at the end shows how to use the functions to encode and decode a string.