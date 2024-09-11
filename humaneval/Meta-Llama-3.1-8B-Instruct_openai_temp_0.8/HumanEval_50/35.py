```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Characters that are not in lowercase are left as is.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5 + 26) % 26 + ord("a")) if ch.isalpha() and ch.islower() else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_shift("hello")
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script includes the `encode_shift` and `decode_shift` functions as requested, along with example usage in the `if __name__ == "__main__":` block. The `encode_shift` function shifts every lowercase letter in the input string by 5 positions in the alphabet, preserving non-alphabet characters. The `decode_shift` function reverses the shift, converting the encoded string back to its original form.