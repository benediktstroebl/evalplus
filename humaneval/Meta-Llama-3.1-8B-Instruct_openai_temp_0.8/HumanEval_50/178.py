```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that all characters in the string are lowercase
    letters. If the string contains other characters, their ASCII values will 
    be shifted, but the result will not be a valid alphabetical character.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that all characters in the string are lowercase
    letters. If the string contains other characters, their ASCII values will 
    be decoded, but the result will not be a valid alphabetical character.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Testing the functions
s = "hello"
encoded_s = encode_shift(s)
decoded_s = decode_shift(encoded_s)

print(f"Encoded string: {encoded_s}")
print(f"Decoded string: {decoded_s}")
```

This script first defines the `encode_shift` function, which shifts every character in the input string by 5 positions in the alphabet. The `decode_shift` function takes the encoded string as input and shifts each character back by 5 positions, effectively reversing the encoding. The script then tests these functions with a sample string "hello" and prints both the encoded and decoded results.