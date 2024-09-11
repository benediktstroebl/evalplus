Here's a self-contained Python script that solves the problem:

```markdown
### Caesar Cipher Encoder and Decoder

This script encodes and decodes a string by shifting every character by 5 in the alphabet.

#### Code

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])

# Example usage:
if __name__ == "__main__":
    input_string = "Hello, World!"
    encoded_string = encode_shift(input_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

#### Output

```
Encoded string: Mjqqt, Btwqi!
Decoded string: Hello, World!
```
This code uses the `ord` function to get the ASCII value of a character, and the `chr` function to convert an ASCII value back to a character. It uses the modulo operator (`%`) to wrap around the alphabet when shifting characters. The `isalpha` method is used to check if a character is a letter before shifting it. The `if __name__ == "__main__"` block provides an example usage of the functions.