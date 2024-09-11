### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    The function splits the input string into groups of three characters each.
    If a group does not have exactly three characters, it remains unchanged.
    Finally, the function cycles the characters within each group, unless the group does not have three characters.
    """
    # split string to groups. Each of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    The function works by splitting the input string back into groups of characters.
    Since each group in the encoded string was cycled by one character when it had three characters,
    this function also cycles each group by one character when it has three characters.
    """
    # split encoded string to groups. Each of length 3
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # decode each group. If group has three elements, cycle by one character
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "hello world"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script includes two functions, `encode_cyclic` and `decode_cyclic`, which perform cyclic encoding and decoding on a given string, respectively. The `encode_cyclic` function splits the input string into groups of three characters each, cycles the characters within each group (unless the group has fewer than three characters), and then returns the encoded string. The `decode_cyclic` function works in reverse, cycling each group of three characters by one character to restore the original string. The example usage demonstrates how to use these functions on a sample string.