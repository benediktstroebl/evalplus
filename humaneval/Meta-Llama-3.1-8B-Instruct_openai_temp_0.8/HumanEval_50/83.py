### Encoding and Decoding Shift Algorithm

Below is a Python script that implements the `encode_shift` and `decode_shift` functions.

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes all characters in the input string are lowercase letters.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes all characters in the input string are lowercase letters.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example use cases
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    print(f"Decoded string: {decoded_string}")
```

This script uses the ASCII values of characters to shift the letters in the input string by 5 positions. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value.

Note that this script assumes all characters in the input string are lowercase letters, and it does not handle any other characters. If you need to handle uppercase letters or other characters, you can modify the script accordingly.