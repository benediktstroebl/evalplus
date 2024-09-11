```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes the input string is a lowercase English alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes the input string is a lowercase English alphabet.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    s = "hello"
    encoded = encode_shift(s)
    print(f"Encoded: {encoded}")
    decoded = decode_shift(encoded)
    print(f"Decoded: {decoded}")
```

In this script, we have added a condition to the list comprehension to check if each character in the string is an alphabet `ch.isalpha()`. This ensures that the `ord` function does not throw an error when encountering non-alphabet characters.