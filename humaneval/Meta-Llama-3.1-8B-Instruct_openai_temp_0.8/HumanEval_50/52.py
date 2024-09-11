```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string only contains lowercase English letters.
    If the input contains uppercase letters or other characters, they will be shifted but will still be uppercase or will end up as a different character.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string only contains lowercase English letters that were encoded with the encode_shift function.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
input_string = "hello"
encoded_string = encode_shift(input_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_shift(encoded_string)
print(f"Decoded string: {decoded_string}")
```

In this code block, I've completed the `decode_shift` function and added some docstrings for clarity. I've also added example usage at the end to demonstrate how to use the functions. The `decode_shift` function works by shifting the characters back by 5 places in the alphabet. Note that the `ord("a")` and `ord("z")` constants are used to handle the wrap-around cases when the shift would exceed the alphabet size.