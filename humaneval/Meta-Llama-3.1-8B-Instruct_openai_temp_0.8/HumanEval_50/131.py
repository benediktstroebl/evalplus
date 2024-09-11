```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


def main():
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")


if __name__ == "__main__":
    main()
```

This Python script defines two functions `encode_shift` and `decode_shift` to encode and decode strings by shifting every alphabet character by 5 positions. The `main` function demonstrates how to use these functions with a sample string. The encoding function takes care to preserve non-alphabet characters by leaving them unchanged. The decoding function is symmetric to the encoding function and can correctly decode a string that was encoded using the `encode_shift` function.