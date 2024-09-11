```markdown
### Caesar Cipher Decoder

This script encodes and decodes strings using a Caesar Cipher with a shift of 5.

#### Code

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): String to encode.
    
    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A") + 5) % 26) + ord("A")) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
        s (str): String to decode.
    
    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A") - 5) % 26) + ord("A")) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

#### Explanation

This script defines two functions: `encode_shift` and `decode_shift`. Both functions use the Caesar Cipher algorithm to shift characters in the input string by 5 positions.

The `encode_shift` function works as follows:

- For lowercase letters, it calculates the new character by shifting the ASCII value of the character by 5.
- For uppercase letters, it calculates the new character by shifting the ASCII value of the character by 5.
- For non-alphabetic characters, it leaves the character unchanged.

The `decode_shift` function works similarly, but with a shift of -5, effectively reversing the encoding.

The example usage at the end of the script shows how to use these functions to encode and decode a string.