```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by converting each character in the string to its ASCII value,
    adding 5 (since 'a' has an ASCII value of 97), taking the result modulo 26 (the number
    of letters in the alphabet), and then converting the result back to a character.
    
    Parameters:
    s (str): The string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by shifting the characters back by 5 in the alphabet.
    
    Parameters:
    s (str): The encoded string.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])


# Test the functions
encoded = encode_shift("hello world")
print(f"Encoded: {encoded}")

decoded = decode_shift(encoded)
print(f"Decoded: {decoded}")
```

This script defines two functions, `encode_shift` and `decode_shift`, that implement the Caesar cipher. The `encode_shift` function shifts every letter in the input string by 5 places to the right in the alphabet, while the `decode_shift` function shifts the letters back by 5 places to the left. The functions only operate on letters, ignoring any other characters in the string. The test code at the end demonstrates how to use these functions by encoding and then decoding the string "hello world".