```markdown
### Cyclic Encoding and Decoding
#### Problem Statement

Encode and decode a string by cycling groups of three characters.

#### Solution

```python
def encode_cyclic(s: str):
    """
    Encode the input string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    # Split the string into groups of three characters. If the string length is not divisible by three, 
    # the last group will have fewer characters.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless the group has fewer elements than three.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    # Join the groups into a single string.
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decode the input string, which was encoded using the encode_cyclic function.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    # Split the string into groups of three characters.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Decode each group by cycling the characters. Unless the group has fewer characters than three.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    # Join the decoded groups into a single string.
    return "".join(groups)
```

#### Example Usage

```python
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded String: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded String: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, which perform the cyclic encoding and decoding of a string, respectively. The example usage demonstrates how to use these functions to encode and decode a sample string.