Here is the self-contained Python script that solves the problem in a markdown code block:

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string only contains lowercase letters.
    If the input string contains uppercase letters or other characters, they will be treated as if they were lowercase.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string only contains lowercase letters.
    If the input string contains uppercase letters or other characters, they will be treated as if they were lowercase.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s.lower()])

# Example usage:
encoded_str = encode_shift("hello")
print(f"Encoded string: {encoded_str}")

decoded_str = decode_shift(encoded_str)
print(f"Decoded string: {decoded_str}")
```

This Python script defines two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher with a shift of 5. The `encode_shift` function takes a string as input, shifts each character by 5 positions in the alphabet, and returns the encoded string. The `decode_shift` function takes a string as input, shifts each character back by 5 positions in the alphabet, and returns the decoded string. The script also includes an example usage of these functions to illustrate how they work.