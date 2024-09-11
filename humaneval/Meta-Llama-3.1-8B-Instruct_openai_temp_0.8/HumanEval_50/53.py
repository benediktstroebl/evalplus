Here's the self-contained Python script that solves the problem:

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 26 - 5) % 26 + ord("a")) for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    encoded = encode_shift("hello")
    decoded = decode_shift(encoded)
    
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")
```

**Explanation:**

*   Both the `encode_shift` and `decode_shift` functions work on lowercase letters, as they depend on the ASCII values of characters.
*   The `encode_shift` function shifts each character by 5 places in the alphabet by calculating the new character index using the formula: `(ord(ch) - ord('a') + 5) % 26`.
*   The `decode_shift` function reverses the encoding process by calculating the new character index using the formula: `(ord(ch) - ord('a') + 26 - 5) % 26`.
*   In the example usage, we first encode the string "hello" and then decode the resulting string to demonstrate the functionality.