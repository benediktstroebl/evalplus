### Cyclic Encoding and Decoding in Python
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
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # decode each group
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)


def test_encoding_decoding():
    # test case 1: string of length 6
    encoded = encode_cyclic("abcdefgh")
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")

    # test case 2: string of length 9
    encoded = encode_cyclic("abcdefghiabcdefgh")
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")

    # test case 3: string of length 3
    encoded = encode_cyclic("abc")
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")

    # test case 4: string of length less than 3
    encoded = encode_cyclic("a")
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")


if __name__ == "__main__":
    test_encoding_decoding()
```
This script defines the `encode_cyclic` and `decode_cyclic` functions as specified, along with a `test_encoding_decoding` function to test the encoding and decoding process with different strings.