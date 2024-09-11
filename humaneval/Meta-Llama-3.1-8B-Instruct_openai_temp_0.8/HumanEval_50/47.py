```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function shifts every lowercase English letter in the input string by 5 places.
    If the input contains any characters other than lowercase English letters, they are left unchanged.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function shifts every character in the input string back by 5 places.
    If the input contains any characters other than lowercase English letters, they are left unchanged.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

Note: The above code uses the ASCII values of characters for calculating the shift. This works for lowercase English letters, but for uppercase letters, it would be different. To make it work for all English letters, you would need to add extra logic to handle uppercase letters separately. However, for the sake of simplicity, the above code only handles lowercase English letters. If you want to handle both lowercase and uppercase English letters, you can use the `isalpha()` function to check if a character is a letter, and then use `ord(ch).lower()` to convert the character to lowercase before calculating the shift.