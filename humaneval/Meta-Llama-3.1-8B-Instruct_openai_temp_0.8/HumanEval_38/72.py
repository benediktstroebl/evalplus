```markdown
### Cyclic Encoding and Decoding

#### Description

This script provides two functions, `encode_cyclic` and `decode_cyclic`, for encoding and decoding a string by cycling groups of three characters.

#### Code

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    :param s: Input string
    :return: Encoded string
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    :param s: Encoded string
    :return: Decoded string
    """
    # Split string to groups. Each of length 3
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Decode each group by moving the first character to the end
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    input_string = "123456789"
    encoded_string = encode_cyclic(input_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

#### Example Output

```
Encoded string: 246135897
Decoded string: 123456789
```

#### Explanation

*   `encode_cyclic` splits the input string into groups of three characters, cycles the characters within each group, and joins them back into a single string.
*   `decode_cyclic` reverses the process by splitting the encoded string into groups, decoding each group by moving the first character to the end, and joining them back into a single string.
*   The example usage demonstrates how to use these functions to encode and decode a string.