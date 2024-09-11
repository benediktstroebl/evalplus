### Shift Cipher Encoder and Decoder

Below is a Python script that includes the `encode_shift` and `decode_shift` functions, along with a `main` function to demonstrate their usage.

```markdown
### Shift Cipher Encoder and Decoder

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def main():
    # Test the functions
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded String: {decoded_string}")

if __name__ == "__main__":
    main()
```

### Explanation:

- The `encode_shift` function shifts every alphabetical character in the input string by 5 places in the alphabet. It checks if a character is a letter before shifting it, and preserves non-alphabetical characters.
- The `decode_shift` function is the inverse of `encode_shift`. It shifts every alphabetical character in the input string by 5 places in the opposite direction to reverse the encoding.
- The `main` function demonstrates the usage of the `encode_shift` and `decode_shift` functions by encoding and decoding the string "Hello, World!".

### Usage:

- Simply run the script. The encoded and decoded strings will be printed to the console.