### Cyclic Encoding and Decoding in Python
#### Problem Description
This script provides a solution to cyclically encode and decode a string by cycling groups of three characters.

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
    
    # Cycle elements in each group. Unless group has fewer elements than 3.
    # Since groups are already decoded, we just need to rotate the first character to the end.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    
    return "".join(groups)

# Example usage:
if __name__ == "__main__":
    original_string = "abcdefgh"
    encoded_string = encode_cyclic(original_string)
    decoded_string = decode_cyclic(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```
#### Explanation
This script consists of two main functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and splits it into groups of three characters. It then cycles the elements in each group (except for groups with fewer than three elements). The `decode_cyclic` function does the opposite, rotating the first character of each group to the end to retrieve the original string.

In the example usage, we demonstrate the encoding and decoding process with the string "abcdefgh". The encoded string is then decoded back to the original string.