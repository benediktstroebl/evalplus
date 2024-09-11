```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): string to be encoded
    
    Returns:
    str: encoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): string to be decoded
    
    Returns:
    str: decoded string
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


def main():
    # Example usage of the functions
    s = "hello"
    encoded = encode_shift(s)
    decoded = decode_shift(encoded)
    
    print(f"Original string: {s}")
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")


if __name__ == "__main__":
    main()
```

This script defines two functions, `encode_shift` and `decode_shift`, to shift every character in a string by 5 positions in the alphabet. The `main` function demonstrates how to use these functions to encode and decode a string. Note that the functions use the ASCII value of 'a' to calculate the shift, which handles both lowercase and uppercase letters. The `lower` method is used to ensure that the function works for both cases.