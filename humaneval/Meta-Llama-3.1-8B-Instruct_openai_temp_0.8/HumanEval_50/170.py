```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


# Example usage:
input_string = "Hello, World!"
encoded = encode_shift(input_string)
decoded = decode_shift(encoded)
print(f"Input: {input_string}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```

This script defines the `encode_shift` and `decode_shift` functions as described. It then demonstrates their usage by encoding the string "Hello, World!", decoding the encoded result, and printing the input, encoded, and decoded strings. The functions will iterate over each character in the input string, shifting alphabetic characters by 5 places in the alphabet and leaving other characters unchanged. The `isalpha` method is used to check if a character is alphabetic, and the `lower` method is used to ensure the functions work correctly for both uppercase and lowercase letters.