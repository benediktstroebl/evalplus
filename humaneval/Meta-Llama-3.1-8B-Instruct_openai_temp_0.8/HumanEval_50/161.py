```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    result = ""
    for ch in s:
        if ch.isalpha():
            ascii_offset = ord("a") if ch.islower() else ord("A")
            result += chr(((ord(ch) - ascii_offset + 5) % 26) + ascii_offset)
        else:
            result += ch  # non-alphabet characters are left unchanged
    return result

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Encoded string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return encode_shift(s)


# Example usage:
input_string = "Hello, World!"
encoded_string = encode_shift(input_string)
decoded_string = decode_shift(encoded_string)

print(f"Input: {input_string}")
print(f"Encoded: {encoded_string}")
print(f"Decoded: {decoded_string}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabet character in the input string by 5 places in the alphabet, wrapping around from 'z' to 'a' and from 'Z' to 'A'. Non-alphabet characters are left unchanged. The `decode_shift` function is simply a wrapper around `encode_shift`, which can be used to decode a string that was encoded with `encode_shift`. The example usage at the end demonstrates how these two functions can be used to enclose and decode a string.