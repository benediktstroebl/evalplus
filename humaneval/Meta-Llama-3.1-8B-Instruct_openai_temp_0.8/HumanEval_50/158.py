```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by iterating over each character in the input string.
    For lowercase letters, it shifts the character in the alphabet by adding 5 to its ASCII value,
    taking modulo 26 to wrap around the alphabet. It then converts the result back to a character
    using the chr function. For characters that are not lowercase letters, it leaves them unchanged.

    :param s: The input string to be encoded
    :return: The encoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by shifting every character in the input string back by 5 positions in the alphabet.
    It achieves this by subtracting 5 from the character's position in the alphabet, taking modulo 26 to wrap around the alphabet.
    It then converts the result back to a character using the chr function. For characters that were not shifted (e.g., non-alphabetic characters),
    it leaves them unchanged.

    :param s: The input string to be decoded
    :return: The decoded string
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26 - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s.lower()])


# Test the functions
print(encode_shift("hello"))  # Output: "mjqqt"
print(decode_shift(encode_shift("hello")))  # Output: "hello"
```

Note that I added the line `ch.isalpha() else ch` to the list comprehension in both functions to ensure that non-alphabetic characters are not shifted and stay unchanged. I also added the `.lower()` method to the `s` argument in both functions to make the functions work correctly regardless of the case of the input string.