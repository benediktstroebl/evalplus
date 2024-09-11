Here is the completed Python script to solve the problem:
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    The idea is to split the input string into groups of three characters.
    Then, for each group with three characters, we cycle them (i.e., move the first character to the end).
    If a group has fewer than three characters, we leave it as is.
    
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
    
    The idea is to split the input string into groups of maximum length 3.
    Then, for each group with three characters, we cycle them back to their original order (i.e., move the last character to the front).
    If a group has fewer than three characters, we leave it as is.
    
    :param s: The input string to be decoded.
    :return: The decoded string.
    """
    # Split string to groups. Each of length up to 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements back in each group. Unless group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    original_string = "HelloWorld"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script includes the two functions `encode_cyclic` and `decode_cyclic`, as well as an example usage section at the end to demonstrate how to use these functions. The `encode_cyclic` function encodes a string by cycling groups of three characters, while the `decode_cyclic` function decodes a string that was previously encoded with `encode_cyclic`.