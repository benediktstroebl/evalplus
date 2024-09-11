```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    result = ""
    for ch in s:
        # Check if character is lowercase
        if ch.islower():
            # Shift character by 5 and adjust for wrap around
            result += chr(((ord(ch) - ord("a") + 5) % 26) + ord("a"))
        # Check if character is uppercase
        elif ch.isupper():
            # Shift character by 5 and adjust for wrap around, then convert to uppercase
            result += chr(((ord(ch) - ord("A") + 5) % 26) + ord("A")).upper()
        # If the character is not a letter, leave it as is
        else:
            result += ch
    return result

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    result = ""
    for ch in s:
        # Check if character is lowercase
        if ch.islower():
            # Shift character by 5 in reverse and adjust for wrap around
            result += chr(((ord(ch) - ord("a") - 5) % 26) + ord("a"))
        # Check if character is uppercase
        elif ch.isupper():
            # Shift character by 5 in reverse and adjust for wrap around, then convert to uppercase
            result += chr(((ord(ch) - ord("A") - 5) % 26) + ord("A")).upper()
        # If the character is not a letter, leave it as is
        else:
            result += ch
    return result

# Example usage
encoded_str = encode_shift("Hello, World!")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This script includes both the `encode_shift` and `decode_shift` functions. The `encode_shift` function shifts each character in the input string by 5 in the alphabet, wrapping around for letters that are shifted beyond 'z' or 'Z'. The `decode_shift` function reverses the encoding process, shifting each character back by 5. Non-letter characters are left unchanged. The script then demonstrates the usage of these functions with the string "Hello, World!".