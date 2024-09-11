```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every letter by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
def main():
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")


if __name__ == "__main__":
    main()
```

In this script:

*   The `encode_shift` function takes a string as input and shifts every lowercase letter by 5 positions in the alphabet. Non-alphabetic characters remain unchanged.
*   The `decode_shift` function takes a string as input that was encoded using the `encode_shift` function. It shifts every lowercase letter back by 5 positions in the alphabet and leaves non-alphabetic characters unchanged.
*   The `main` function demonstrates the usage of these two functions by encoding the string "Hello, World!", printing the encoded string, and then decoding it to retrieve the original string.