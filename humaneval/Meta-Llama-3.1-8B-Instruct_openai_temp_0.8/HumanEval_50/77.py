```markdown
### Shift Encoder and Decoder in Python

This script includes two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns a new string where every character is shifted by 5 places in the alphabet. The `decode_shift` function takes a string encoded with `encode_shift` and returns the original string.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    :param s: Input string to be encoded
    :return: Encoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    :param s: Input string to be decoded
    :return: Decoded string
    """
    return "".join([chr(((ord(ch) - ord("a") + 25 - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
original_string = "Hello World!"
encoded_string = encode_shift(original_string)
decoded_string = decode_shift(encoded_string)

print(f"Original String: {original_string}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded String: {decoded_string}")
```

### Explanation:

*   The `ord` function is used to get the ASCII value of a character.
*   The `chr` function is used to get the character represented by a specific ASCII value.
*   The expression `(ord(ch) - ord("a") + 5) % 26` is used to shift the character by 5 places in the alphabet. The `% 26` operation is used to wrap around the alphabet when shifting past 'z' or 'Z'.
*   The `lower` method is used to ensure the function works with both lowercase and uppercase letters.
*   The `isalpha` method is used to filter out non-alphabet characters.

This script demonstrates a basic implementation of the Caesar cipher encryption technique, which shifts each letter in the plaintext by a fixed number of positions down the alphabet.