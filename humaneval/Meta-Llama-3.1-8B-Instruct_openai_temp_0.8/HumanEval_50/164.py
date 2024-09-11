```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character in the input string to its corresponding ASCII value.
    It then calculates the new character by shifting the ASCII value by 5, taking into account the wrap around.
    Finally, it converts the new ASCII value back to a character and joins all the characters together to form the encoded string.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by first converting each character in the input string to its corresponding ASCII value.
    It then calculates the new character by shifting the ASCII value by 5 in the opposite direction, taking into account the wrap around.
    Finally, it converts the new ASCII value back to a character and joins all the characters together to form the decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
input_str = "Hello, World!"
encoded_str = encode_shift(input_str)
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script defines two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher algorithm to encode and decode strings by shifting every character by 5 in the alphabet. The `encode_shift` function shifts the characters in the input string to the right by 5, while the `decode_shift` function shifts them back to the left by 5. The script also demonstrates the usage of these functions with an example string.