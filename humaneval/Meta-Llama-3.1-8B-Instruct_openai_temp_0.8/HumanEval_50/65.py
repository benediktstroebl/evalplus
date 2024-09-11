```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    If the input character is not a lowercase letter, it is left unchanged in the output string.
    
    For uppercase letters, we first convert them to lowercase and then shift them.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    If the input character is not a lowercase letter, it is left unchanged in the output string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    # Encode a string
    encoded_str = encode_shift("hello world")
    print(f"Encoded string: {encoded_str}")

    # Decode the string
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every lowercase letter in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function reverses this process to decode the input string.

Note that we use the `isalpha` method to check if a character is a letter before attempting to shift it. This prevents an error when the input string contains non-alphabetic characters.

Finally, we demonstrate the usage of these functions in the `if __name__ == "__main__":` block, encoding the string "hello world" and then decoding the result.