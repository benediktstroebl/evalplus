```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function works assuming the input string contains only lowercase letters.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    encoded_string = encode_shift("hello")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_shift` and `decode_shift`, which encode and decode a given string, respectively, by shifting every character by 5 in the alphabet. The `isalpha` method is used to filter out non-alphabet characters from the input string. The example usage demonstrates how to use these functions.