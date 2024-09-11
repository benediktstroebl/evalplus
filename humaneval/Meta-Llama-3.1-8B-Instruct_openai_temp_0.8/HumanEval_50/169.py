```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string only contains lowercase English letters.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()]) 

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string only contains lowercase English letters.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()]) 


# Test the functions
original_string = "hello"
encoded_string = encode_shift(original_string)
print(f"Original string: {original_string}")
print(f"Encoded string: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```

Note: This is an implementation of the Caesar Cipher encryption technique, where each letter in the plaintext is'shifted' a certain number of places down the alphabet. In this case, we shift by 5 places.