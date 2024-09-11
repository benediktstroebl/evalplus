```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    For example:
    - Input: 'abcdefg'
    - Output: 'bade bgcf'
    
    :param s: String to be encoded
    :return: Encoded string
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Encoded string
    :return: Decoded string
    """
    # split encoded string to groups
    groups = s.split()
    # decode each group by cycling elements back to their original order
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    # join decoded groups back into string
    return "".join(decoded_groups)


# example usage
if __name__ == "__main__":
    encoded_str = encode_cyclic('abcdefg')
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input, splits it into groups of three characters, cycles the elements in each group (unless there are fewer than three elements), and returns the encoded string. The `decode_cyclic` function reverses this process to decode the input string.

The example usage at the bottom of the script demonstrates how to use these functions to encode and decode a string.