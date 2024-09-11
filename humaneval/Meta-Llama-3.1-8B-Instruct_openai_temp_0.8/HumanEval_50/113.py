```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by converting each character to its ASCII value, 
    adding 5 to it (but adjusting the value to be within the range of lowercase 
    letters by subtracting the ASCII value of 'a'), taking the modulus of this 
    value with 26 to wrap around the alphabet, and then converting it back to a 
    character using the chr function.

    Parameters:
    s (str): The string to be encoded.

    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by reversing the process of the encode_shift function. It 
    converts each character to its ASCII value, subtracts 5 from it (but adjusts 
    the value to be within the range of lowercase letters by adding the ASCII value 
    of 'a' and then taking the modulus with 26 to wrap around the alphabet), and 
    then converts it back to a character using the chr function.

    Parameters:
    s (str): The string to be decoded.

    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Test the functions
print(f"Encoded string: {encode_shift('Hello World')}")
print(f"Decoded string: {decode_shift(encode_shift('Hello World'))}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns a string where every character has been shifted by 5 positions in the alphabet. The `decode_shift` function takes a string as input and returns the original string, having shifted the characters back by 5 positions.

The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to convert an ASCII value back to a character. The `lower` function is used to ensure the function works with both lowercase and uppercase letters, and the `isalpha` function is used to ensure the function works with non-alphabetic characters (like spaces). The `% 26` operation is used to wrap around the alphabet when shifting a character.