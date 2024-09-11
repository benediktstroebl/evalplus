```markdown
### Shift Encoder and Decoder

#### Problem Description
Shift every character in a given string by 5 positions in the alphabet.

#### Code

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example Usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

#### Explanation

*   The `encode_shift` function takes a string `s` as input and returns the encoded string.
*   It uses a list comprehension to iterate over each character `ch` in the input string.
*   The `ord` function is used to get the ASCII value of each character.
*   The ASCII value of 'a' is subtracted from the character's ASCII value to shift the character to a position where 'a' has an ASCII value of 0.
*   The result is then added to 5 and the modulus operator `% 26` is applied to ensure the result remains within the range of lowercase English letters (0-25).
*   The `chr` function is used to convert the resulting value back to a character.
*   The `join` function is used to concatenate the encoded characters into a single string.
*   The `isalpha` function is used to check if a character is a letter, and the `lower` function is used to ensure the function works correctly for both lowercase and uppercase letters.
*   The `decode_shift` function is similar to the `encode_shift` function but subtracts 5 instead of adding 5 to decode the string.
*   In the example usage, the original string "Hello, World!" is encoded using the `encode_shift` function and then decoded using the `decode_shift` function to demonstrate the functionality of the functions.
```