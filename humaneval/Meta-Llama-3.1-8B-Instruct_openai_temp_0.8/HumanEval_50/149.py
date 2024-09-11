```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    The function works by converting every lowercase character in the input string
    to its ASCII value, adding 5 (modulo 26 to handle uppercase letters), and then
    converting the result back to a character. The result is a string where every
    character is shifted by 5 places in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    The function works by converting every character in the input string to its
    ASCII value, subtracting 5 (modulo 26 to handle uppercase letters), and then
    converting the result back to a character. The result is a string where every
    character is shifted back by 5 places in the alphabet.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print("Original string:", original_string)
    print("Encoded string:", encoded_string)
    print("Decoded string:", decoded_string)
```

In this code, we use the `ord()` function to get the ASCII value of a character, and `chr()` to get the character represented by a specific ASCII value. We use the modulo operator (`% 26`) to handle cases where the shift would take us past the end of the alphabet.

We also added a check using the `isalpha()` method to ensure that we only try to shift letters, and leave other characters (like spaces and punctuation) unchanged.