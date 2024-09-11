```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function shifts each character in the string by 5 positions in the alphabet.
    If a character is 'z', 'Z', or any character that is not in the alphabet, it remains unchanged.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch 
                    for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function shifts each character in the string by 5 positions backwards in the alphabet.
    If a character is 'z', 'Z', or any character that is not in the alphabet, it remains unchanged.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() else ch 
                    for ch in s])


def main():
    original_string = "hello world"
    print("Original string:", original_string)
    
    encoded_string = encode_shift(original_string)
    print("Encoded string:", encoded_string)
    
    decoded_string = decode_shift(encoded_string)
    print("Decoded string:", decoded_string)


if __name__ == "__main__":
    main()
```

This script defines two functions, `encode_shift` and `decode_shift`, that encodes and decodes a string by shifting each character by 5 positions in the alphabet. The `main` function demonstrates how to use these functions.