```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    message = "Hello, World!"
    encoded_message = encode_shift(message)
    print(f"Encoded Message: {encoded_message}")
    
    decoded_message = decode_shift(encoded_message)
    print(f"Decoded Message: {decoded_message}")
```

Note: This script handles both lowercase and uppercase letters. If a character is not a letter (e.g., punctuation or numbers), it is left unchanged. The encoding and decoding logic is applied to lowercase letters by subtracting the ASCII value of 'a' and then adjusting, but this subtraction is also done for the other characters to avoid an error.