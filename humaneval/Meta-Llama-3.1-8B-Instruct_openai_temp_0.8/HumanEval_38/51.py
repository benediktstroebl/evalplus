### Cyclic Encoding and Decoding

Below is a Python script that includes the `encode_cyclic` and `decode_cyclic` functions to encode and decode a string by cycling groups of three characters.

```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. 
    Returns decoded string.
    """
    # Since the encode function adds the first character to the end of each group
    # of 3, we add the first character of each group to the beginning
    # of the group and remove the last character of each group.
    groups = [s[(3 * i):3 * (i + 1)] + s[(3 * i):(3 * i + 1)] for i in range((len(s) + 1) // 3)]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

This script will output the original string, the encoded string, and the decoded string for the example usage. The `encode_cyclic` function cycles the characters within groups of three, and the `decode_cyclic` function reverses this process to recover the original string.