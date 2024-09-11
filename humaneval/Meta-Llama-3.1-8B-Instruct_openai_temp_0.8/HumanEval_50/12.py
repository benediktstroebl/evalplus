### Shift Encoder and Decoder

Below is a Python script that includes the `encode_shift` function to encode a string by shifting every character by 5 in the alphabet and the `decode_shift` function to decode a string that was previously encoded using `encode_shift` function.

```markdown
### Shift Encoder and Decoder

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Example usage:
original_string = "Hello, World!"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

### Explanation:

- The `encode_shift` function shifts every alphabetic character in the input string by 5 positions forward in the alphabet.
- The `decode_shift` function shifts every alphabetic character in the input string by 5 positions backward in the alphabet.
- The `ord` function is used to get the ASCII value of a character and `chr` to get the character represented by a specific ASCII value.
- The `isalpha` function checks if a character is alphabetic. Non-alphabetic characters are preserved in their original form.
- The `lower` function is used to convert the input string to lowercase to simplify the alphabet shifting process.
- The example usage demonstrates the encoding and decoding of a string.