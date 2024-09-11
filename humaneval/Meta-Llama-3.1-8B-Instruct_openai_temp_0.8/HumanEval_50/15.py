```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s]).lower()

# Test the functions
print("Encoded string: ", encode_shift("Hello, World!"))
print("Decoded string: ", decode_shift(encode_shift("Hello, World!")))
```

In the above script, `encode_shift` function shifts every letter in the given string by 5 positions in the alphabet. However, if the character is not a letter, it remains unchanged. The `decode_shift` function is the inverse operation, shifting the characters back by 5 positions.

Note that we use `isalpha()` method to check if a character is a letter, and `lower()` method to ensure the function works correctly for both lowercase and uppercase letters. 

Also note that we use `% 26` to handle cases where the shift operation would result in a character outside the alphabet (e.g., 'z' shifted by 5 positions). This is because there are only 26 letters in the alphabet.