```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character in the string to its corresponding ASCII value. 
    Then, it calculates the shifted value by adding 5 to the ASCII value of 'a' and subtracting the ASCII value of the character. 
    The result is taken modulo 26 to ensure it stays within the range of the alphabet. 
    Finally, the shifted value is converted back to a character using the chr function and added to the result string.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works similarly to encode_shift, but it subtracts 5 from the shifted value instead of adding it.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

# Example usage:
encoded_str = encode_shift("Hello, World!")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script defines the `encode_shift` and `decode_shift` functions according to your specifications. It also includes example usage at the end to demonstrate how to use these functions. The `encode_shift` function now correctly handles both uppercase and lowercase letters, and it filters out non-alphabetic characters.