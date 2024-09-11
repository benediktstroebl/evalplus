Here is a self-contained Python script that solves the problem:

```markdown
## Shift Encoder/Decoder
### Problem Description
This script provides a solution to shift every character in a given string by 5 places in the alphabet for encoding, and reverses the transformation to decode the string.

### Code

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s if ch.isalpha()])


# Example usage
if __name__ == "__main__":
    # Test encoding and decoding
    input_str = "Hello World"
    encoded_str = encode_shift(input_str)
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

### Explanation
- The `encode_shift` function takes a string `s` as input and shifts each alphabet character by 5 places in the alphabet. The `% 26` operation ensures the shift wraps around the alphabet.
- The `decode_shift` function takes a string `s` as input, which is assumed to be encoded with `encode_shift`. It shifts each alphabet character by 5 places in the opposite direction to reverse the encoding.
- The `isalpha()` function is used to check if a character is an alphabet letter, and only such characters are processed.
- In the example usage, we test the encoding and decoding functions with the string "Hello World" and print the results.