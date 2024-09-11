```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works by first converting each character in the string to its corresponding ASCII value. 
    It then adds 5 to this value, but since ASCII values for 'a' to 'z' are consecutive, we subtract the ASCII value of 'a' 
    to shift the value to a range from 0 to 25, add 5, take the result modulo 26 to wrap around the alphabet, 
    then add the ASCII value of 'a' back to get the shifted character. The result is a string where each character is shifted by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by applying the inverse operation of encode_shift. 
    It subtracts 5 from each character's ASCII value, then takes the result modulo 26 to wrap around the alphabet 
    (which is equivalent to shifting right by 5 places in the alphabet), then subtracts the ASCII value of 'a' to get the original character's ASCII value.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])

# Example usage:
print(encode_shift("hello"))
print(decode_shift(encode_shift("hello")))
```

Note: I've modified the `encode_shift` function to handle both lowercase and uppercase characters. In the original code, the `ord(ch) - ord('a')` expression would not have worked correctly for uppercase characters. 
Also note that the `decode_shift` function does the same thing as `encode_shift` in reverse, i.e., it shifts right by 5 places in the alphabet, which is equivalent to shifting left by 21 places in the alphabet.