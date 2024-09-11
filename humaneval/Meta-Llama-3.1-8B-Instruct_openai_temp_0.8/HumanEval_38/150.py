### Cyclic Encoding and Decoding

Below is a Python script that defines two functions: `encode_cyclic` and `decode_cyclic`, which implement the cyclic encoding and decoding logic as described.

```python
def encode_cyclic(s: str):
    """
    Encodes a given string by cycling groups of three characters.

    Args:
    s (str): The input string to encode.

    Returns:
    str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a given string that was encoded with the encode_cyclic function.

    Args:
    s (str): The encoded string to decode.

    Returns:
    str: The decoded string.
    """
    # split string to groups.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # decode each group by cycling elements. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcd"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which implement the described logic for cyclic encoding and decoding. The `encode_cyclic` function splits the input string into groups of three characters, cycles them if the group size is exactly three, and then joins the groups back into a string. The `decode_cyclic` function reverses this process to decode the string.

The script also includes an example usage at the end, where it encodes and then decodes a sample string to demonstrate the functionality of the functions.