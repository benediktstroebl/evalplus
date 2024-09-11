```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    If the shift occurs past 'z' or 'Z', it will wrap around to the beginning of the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A") + 5) % 26) + ord("A")) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26) + 25 - 5) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A")) % 26) + 25 - 5) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])

# Example usage
print(encode_shift("Hello, World!"))
print(decode_shift(encode_shift("Hello, World!")))
```

Note: In the `encode_shift` function, I have added conditions to handle uppercase and lowercase letters separately. This is because the ASCII values for uppercase and lowercase letters differ by 32. The `ord` function in Python returns the ASCII value of a character. The `chr` function returns the character represented by a specified ASCII value. The modulo operation (`% 26`) is used to ensure that the shift wraps around to the beginning of the alphabet. In the `decode_shift` function, I have used a similar approach but with a different calculation to reverse the shift.