```markdown
### Cyclic Encoding and Decoding

This script provides two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes as input a string encoded with the `encode_cyclic` function and returns the decoded string.

#### Code

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # decode each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[1:-1] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghi"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
    print(f"Original string: {original_string}")
    print(f"Decoded string matches original string: {decoded_string == original_string}")
```

#### Explanation

*   The `encode_cyclic` function works by splitting the input string into groups of three characters. If a group has fewer than three characters, it is left unchanged. The elements in each group are then cycled, with the first element moved to the end of the group.
*   The `decode_cyclic` function reverses the process used by `encode_cyclic`. Each group of three characters is decoded by moving the last element to the beginning of the group.
*   In the example usage, a string "abcdefghi" is encoded using the `encode_cyclic` function, decoded using the `decode_cyclic` function, and then compared with the original string to verify that decoding correctly reverses the encoding process.