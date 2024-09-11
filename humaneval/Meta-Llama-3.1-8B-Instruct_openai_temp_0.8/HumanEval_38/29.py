### Cyclic Encoding and Decoding in Python
#### Problem Description

This script implements two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes the encoded string as input and returns the original decoded string.

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
    # Ensure the string length is a multiple of 3 for simplicity
    if len(s) % 3!= 0:
        s += " " * ((3 - len(s) % 3) % 3)

    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]

    # Join the groups into a single string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a string that was encoded using the encode_cyclic function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Split the string into groups
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]

    # Reverse the cycle in each group
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]

    # Join the groups into a single string
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)

    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

#### Explanation

1.  The `encode_cyclic` function first checks if the input string length is a multiple of 3. If not, it pads the string with spaces to make its length a multiple of 3 for simplicity.
2.  It then splits the string into groups of three characters using a list comprehension.
3.  The function cycles the elements in each group by using the `if len(group) == 3` condition. This condition checks if the group has exactly three characters, and if so, it cycles the characters by moving the first character to the end of the group.
4.  The `decode_cyclic` function reverses the cycle in each group to obtain the original string.
5.  The example usage demonstrates how to use these functions by encoding and decoding a sample string.