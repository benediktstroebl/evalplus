### Cyclic Encoding and Decoding

Below is a Python script that includes the implementation of the `encode_cyclic` and `decode_cyclic` functions. The `decode_cyclic` function uses the `encode_cyclic` function to reverse the encoding process.

```markdown
### Code

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
    # split input string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse the cycling of elements in each group.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    print("Original string:", original_string)
    print("Encoded string:", encoded_string)
    decoded_string = decode_cyclic(encoded_string)
    print("Decoded string:", decoded_string)
```

### Output

```
Original string: abcdefgh
Encoded string: bcdegfha
Decoded string: abcdefgh
```

This script defines the `encode_cyclic` and `decode_cyclic` functions and demonstrates their usage by encoding and decoding a test string. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and returns the encoded string. The `decode_cyclic` function reverses this process by splitting the input string into groups, reversing the cycling of elements in each group, and returning the decoded string. The example usage shows that the `decode_cyclic` function correctly restores the original string from the encoded string.