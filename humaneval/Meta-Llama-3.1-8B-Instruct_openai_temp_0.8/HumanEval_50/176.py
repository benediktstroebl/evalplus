```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character to its ASCII value.
    It then subtracts the ASCII value of 'a' from the ASCII value of the character,
    adds 5 to the result, takes the modulus with 26 (the number of letters in the alphabet),
    and finally adds the ASCII value of 'a' back to get the new ASCII value.
    
    This process effectively shifts the character 5 places forward in the alphabet.
    
    :param s: The string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function works by first converting each character to its ASCII value.
    It then subtracts the ASCII value of 'a' from the ASCII value of the character,
    subtracts 5 from the result, takes the modulus with 26 (the number of letters in the alphabet),
    and finally adds the ASCII value of 'a' back to get the new ASCII value.
    
    This process effectively shifts the character 5 places backward in the alphabet.
    
    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage:
encoded_str = encode_shift("hello")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script first defines the `encode_shift` function to shift characters in a string 5 places forward in the alphabet, and then the `decode_shift` function to shift characters 5 places backward in the alphabet. The example usage demonstrates how to use these functions to encode and then decode a string.