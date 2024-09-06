Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function shifts each character of an input string by 5 in the alphabet, ensuring that characters beyond 'z' wrap around to 'a'. The `decode_shift` function reverses this process to decode the message. 

Note that these functions assume that the input string only contains English alphabetical characters.