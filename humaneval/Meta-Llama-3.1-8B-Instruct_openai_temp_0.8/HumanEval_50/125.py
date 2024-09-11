```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()]).lower()


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns a new string where each character is shifted by 5 positions in the alphabet. The `decode_shift` function does the opposite, taking an encoded string as input and returning the original string.

Note that the script uses the `ord` function to get the ASCII value of a character and the `chr` function to get the character represented by a specific ASCII value. It also uses the `isalpha` function to check if a character is a letter, and the `lower` function to ensure the input string is converted to lowercase before processing.

The example usage at the end of the script demonstrates how to use these functions to encode and decode a string.