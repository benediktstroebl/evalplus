### Cyclic Encoding and Decoding
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    The function splits the input string into groups of three characters, 
    then rotates each group so that the first character becomes the last and vice versa, 
    unless the group has fewer than three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.

    The function works by splitting the input string into groups of three characters, 
    then rotating each group back to its original order.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups = [(group[2] + group[1] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    original_string = "abcdef"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")

    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, rotates each group to cycle the characters, and returns the encoded string. The `decode_cyclic` function does the reverse, taking an encoded string as input, splitting it into groups of three characters, rotating each group to reverse the cycle, and returning the decoded string.

The example usage at the end demonstrates how to use these functions. It encodes the string "abcdef" using `encode_cyclic`, then decodes the result using `decode_cyclic`, and prints the original and decoded strings for comparison.