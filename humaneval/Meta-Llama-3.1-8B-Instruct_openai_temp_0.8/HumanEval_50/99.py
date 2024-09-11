Here's how you could implement the `decode_shift` function:

```markdown
### Caesar Cipher Decoder

#### Problem Description
The `encode_shift` function shifts every character in a given string by 5 places in the alphabet.
This code provides a way to decode a string that was previously encoded with `encode_shift`.

#### Code

```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + (26 - 5)) % 26) + ord("a") for ch in s.lower() if ch.isalpha()])


def main():
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

#### Explanation

- The `decode_shift` function works by shifting every character back by 5 places in the alphabet.
- Since the shift operation is performed modulo 26 (the number of letters in the alphabet), we can simply subtract 5 from the position of each character in the alphabet.
- We use the `ord` function to get the ASCII value of each character, subtract the ASCII value of 'a' to get the position in the alphabet (0-25), subtract 5, take the modulus 26, add the ASCII value of 'a' back to get the ASCII value of the decoded character, and finally use `chr` to get the character represented by that ASCII value.
- We use the `isalpha` method to ensure we're only shifting alphabetic characters, and we convert the string to lowercase to simplify the calculation.
- In the `main` function, we demonstrate how to use these functions to encode and decode a string.