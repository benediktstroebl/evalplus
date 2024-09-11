### Cyclic Encoding and Decoding
#### Overview
This script implements two main functions, `encode_cyclic` and `decode_cyclic`, which perform cyclic encoding and decoding of a given string. The encoding process splits the string into groups of three characters and cycles them, while the decoding process reverses this process.

#### Code
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
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse cycle in each group. Unless group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    input_string = "abcdef"
    encoded_string = encode_cyclic(input_string)
    print("Encoded String:", encoded_string)

    decoded_string = decode_cyclic(encoded_string)
    print("Decoded String:", decoded_string)

    assert decoded_string == input_string
```
#### Explanation
The `encode_cyclic` function splits the input string into groups of three characters and cycles them. The `decode_cyclic` function reverses this process by splitting the encoded string into groups and reversing the cycle in each group. The example usage demonstrates the encoding and decoding of a sample string.