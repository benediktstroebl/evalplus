```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode groups by cycling elements in reverse order. Unless group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    # join all decoded groups into one string
    return "".join(groups)


# Test the functions
def main():
    s = "HelloWorld"
    encoded = encode_cyclic(s)
    print(f"Encoded: {encoded}")

    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")


if __name__ == "__main__":
    main()
```

This script defines the `encode_cyclic` and `decode_cyclic` functions, and includes a `main` function to test them with the string "HelloWorld". The `main` function encodes the string, prints the encoded string, decodes the string, and prints the decoded string.