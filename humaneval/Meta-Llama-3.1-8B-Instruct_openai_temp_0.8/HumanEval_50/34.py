```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    # Test the functions
    text = "Hello, World!"
    encoded = encode_shift(text)
    print("Encoded:", encoded)

    decoded = decode_shift(encoded)
    print("Decoded:", decoded)
```

This code adds checks to handle both lowercase and uppercase letters correctly, along with non-alphabetical characters. The `ord("a")` and `ord("a") + 5` are used to shift the alphabet letters, while the `ord(ch) - ord("a")` helps us determine the position of each character in the alphabet.