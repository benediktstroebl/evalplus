```python
def encode(message):
    """
    Encodes the message such that all letters' case is swapped and every 
    vowel is replaced with the next letter in the English alphabet.
    Args: 
        message: str, the input message to encode
    Returns: 
        string, the encoded message
    """
    vowels = "aeiouAEIOU"
    encoded = ""
    for char in message:
        if char in vowels:
            encoded += char.else
        else:
            encoded += chr(ord(char) + 1)
    return encoded
```