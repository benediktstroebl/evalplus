```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Note: This function assumes lowercase English alphabets.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Note: This function assumes lowercase English alphabets.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s if ch.isalpha()])


def main():
    original_string = "hello world"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")


if __name__ == "__main__":
    main()
```

In this code, `encode_shift` function shifts every lowercase alphabet in the input string by 5 positions forward in the alphabet. The `decode_shift` function does the reverse operation, shifting by 5 positions backward in the alphabet. Both functions preserve non-alphabet characters and assume only lowercase English alphabets.

Note: The `isalpha` method is used to check if a character is a letter before applying the shift. This is a good practice to prevent `TypeError` in case of non-alphabet characters. 

Also, the `if __name__ == "__main__":` block is used to ensure that the `main` function is only executed when the script is run directly, not when it's imported as a module.