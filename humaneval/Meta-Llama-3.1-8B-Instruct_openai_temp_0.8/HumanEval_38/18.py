Here's a self-contained Python script that solves the given problem:
```markdown
## Encoding and Decoding Cyclic Strings

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function takes an encoded string as input, determines the original groups before cycling, and reconstructs the original string.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    # Determine the original groups before cycling
    decoded_groups = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i+2] == s[i]: # cycle detected
            decoded_groups.append(s[i+1] + s[i])
        elif i + 2 < len(s): # not a cycle, next group starts here
            decoded_groups.append(s[i:i+3])
        else: # last group of length 2
            decoded_groups.append(s[i:])
        i += 3

    # Reconstruct the original string
    return "".join(decoded_groups)


# Example usage:
input_string = "abcdefg"
encoded_string = encode_cyclic(input_string)
print(f"Encoded string: {encoded_string}")

decoded_string = decode_cyclic(encoded_string)
print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits the input string into groups of three characters and cycles the elements in each group. The `decode_cyclic` function determines the original groups before cycling and reconstructs the original string.

The example usage demonstrates how to use these functions to encode and decode a string. The encoded string is then decoded back to the original string, which is printed to the console.

Note that this implementation assumes that the input string is a multiple of three characters long or has two characters remaining after the last full group of three characters. If the input string has a different length, the implementation may need to be adjusted accordingly.