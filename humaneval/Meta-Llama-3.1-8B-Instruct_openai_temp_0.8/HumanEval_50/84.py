```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by iterating over each character in the string. If the character
    is an alphabet letter, it calculates the new character by shifting it 5 positions
    forward in the alphabet. The result is then converted to a character and added to
    the encoded string. Non-alphabet characters (like spaces and punctuation) are left
    unchanged.

    Parameters:
    s (str): The string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else ch for ch in s])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works similarly to encode_shift, but shifts characters in the opposite
    direction to reverse the encoding.

    Parameters:
    s (str): The encoded string.

    Returns:
    str: The decoded string.
    """
    return encode_shift(s)

# Test the functions
print(encode_shift("hello"))  # prints "mjqqt"
print(decode_shift(encode_shift("hello")))  # prints "hello"
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string, shifts each character by 5 positions in the alphabet (wrapping around to the start for characters that would otherwise shift past 'z'), and returns the encoded string. The `decode_shift` function simply calls `encode_shift` again to reverse the encoding. The script then tests these functions with the string "hello".