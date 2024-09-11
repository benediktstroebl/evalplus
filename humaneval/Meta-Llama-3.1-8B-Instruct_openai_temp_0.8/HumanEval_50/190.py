Here's a self-contained Python script that solves the problem in a markdown code block:
```python
def encode_shift(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])

def decode_shift(s: str) -> str:
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch for ch in s.lower()])

# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script defines two functions, `encode_shift` and `decode_shift`, which shift characters in a string by 5 places in the alphabet. The `ord` function is used to get the ASCII value of a character, and the `chr` function is used to get the character represented by a specific ASCII value. The `% 26` operation ensures that the shift wraps around the alphabet.

Note that this script converts the input string to lowercase before applying the shift, and it preserves non-alphabetic characters. The example usage demonstrates how to use these functions to encode and decode a string.