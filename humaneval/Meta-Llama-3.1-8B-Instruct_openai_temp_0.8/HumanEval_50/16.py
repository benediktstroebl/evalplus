```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by first converting each character to its ASCII value, 
    subtracting the ASCII value of 'a' to get the position in the alphabet, 
    shifting the position by 5, taking the modulus 26 to wrap around the alphabet, 
    and then converting back to a character.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by first converting each character to its ASCII value, 
    subtracting the ASCII value of 'a' to get the position in the alphabet, 
    shifting the position back by 5, taking the modulus 26 to wrap around the alphabet, 
    and then converting back to a character.

    Parameters:
    s (str): The input string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage:
print("Encoded string: ", encode_shift("hello"))
print("Decoded string: ", decode_shift("khoor"))
```

Note: The code has been modified to handle both uppercase and lowercase letters by converting the input string to lowercase before encoding or decoding. Also, the `ord(ch) - ord("a")` expression is used to get the position of the character in the alphabet, which is a more concise and readable way to do it.