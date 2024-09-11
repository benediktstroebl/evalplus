### Cyclic Encoding and Decoding in Python

The following script provides solutions to the cyclic encoding and decoding problem using Python. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements within each group, and returns the encoded string. The `decode_cyclic` function takes as input a string encoded with the `encode_cyclic` function, reverses the cycling process, and returns the decoded string.

```markdown
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
    # split encoded string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse cycling in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic("123456789")
    print("Encoded String:", encoded_str)

    decoded_str = decode_cyclic(encoded_str)
    print("Decoded String:", decoded_str)

    assert decoded_str == "123456789"
```

### Explanation:

*   The `encode_cyclic` function first splits the input string into groups of three characters using list comprehension.
*   It then cycles the elements within each group by appending the first element to the end of the remaining elements in the group, unless the group has fewer than three elements.
*   The `decode_cyclic` function reverses the cycling process by prepending the last element to the end of the remaining elements in the group.
*   In the example usage section, we demonstrate the encoding and decoding process with the string "123456789" and verify that the decoded string matches the original string.