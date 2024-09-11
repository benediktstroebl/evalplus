### Cyclic Encoding and Decoding
#### Problem Description
Encode a given string by cycling groups of three characters and provide a function to decode the string.

#### Solution
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
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
        s (str): Input encoded string.

    Returns:
        str: Decoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Cycle elements in each group back to original order
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


# Example usage
if __name__ == "__main__":
    # Test encoding and decoding
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```
This script includes two functions: `encode_cyclic` to encode a string by cycling groups of three characters and `decode_cyclic` to reverse this process. The `if __name__ == "__main__":` block provides a test case to demonstrate the usage of these functions.