```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 26 - 5) % 26) + ord("a")) for ch in s.lower()])


# Example usage
if __name__ == "__main__":
    # Test the functions
    original_string = "Hello World"
    encoded = encode_shift(original_string)
    decoded = decode_shift(encoded)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")
```

In this script, we add the `.lower()` method to ensure that the function works correctly for both lower and upper-case characters. The function now correctly handles lower case letters. 

It is worth noting that the decode_shift function was modified to also handle lower case letters. This modification is achieved by subtracting the ASCII value of 'a' from each character before the modulo operation.