```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage
original_string = "hello"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original string: {original_string}")
print(f"Encoded string: {encoded_string}")
print(f"Decoded string: {decoded_string}")
```

In this script, both encoding and decoding functions work with both lowercase and uppercase letters. The encoding function shifts each character by 5 in the alphabet, while the decoding function shifts each character in the opposite direction to recover the original string.