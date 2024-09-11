Here's a self-contained Python script that solves the problem:

```markdown
### Caesar Cipher Encoder and Decoder

This script provides two functions to encode and decode strings using a Caesar cipher with a shift of 5.

#### encode_shift(s: str)

Encodes a string by shifting every character by 5 in the alphabet.

#### decode_shift(s: str)

Takes as input string encoded with encode_shift function and returns decoded string.

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    encoded_chars = [chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s]
    return "".join(encoded_chars)


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decoded_chars = [chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s]
    return "".join(decoded_chars)


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

### Explanation

The script uses the `ord` function to get the ASCII value of each character in the string. For lowercase letters, the ASCII value is shifted by 5, wrapped around the alphabet using the modulo operator (`% 26`), and converted back to a character using `chr`.

For non-alphabetic characters (such as punctuation and spaces), the original character is left unchanged.

The `decode_shift` function is similar, but it subtracts 5 from the ASCII value instead of adding it, and it also uses a negative shift to undo the encoding.