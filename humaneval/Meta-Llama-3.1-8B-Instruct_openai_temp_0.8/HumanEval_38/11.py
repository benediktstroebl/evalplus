### Cyclic Encoding and Decoding Script

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
    s (str): The encoded string to be decoded.

    Returns:
    str: The decoded string.
    """
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    # Iterate over the encoded groups
    for group in [s[i:i+3] for i in range(0, len(s), 3)]:
        # If the group has fewer elements than 3, append its first character to the next group
        if len(group) < 3:
            if decoded_groups:
                decoded_groups[-1] += group[0]
            else:
                decoded_groups.append(group[0])
        # Otherwise, cycle the group elements
        else:
            decoded_groups.append((group[1:] + group[0]))
    # Join the decoded groups into a single string
    decoded_string = "".join(decoded_groups)
    return decoded_string


# Example usage:
if __name__ == "__main__":
    input_string = "abcdefgh"
    encoded_string = encode_cyclic(input_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this script, the `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group (unless the group has fewer elements than three), and then joins the resulting groups into a single encoded string. The `decode_cyclic` function does the reverse, splitting the encoded string into groups, cycling the elements in each group if necessary, and then joining the resulting groups into a single decoded string. The example usage demonstrates the functionality of these functions.