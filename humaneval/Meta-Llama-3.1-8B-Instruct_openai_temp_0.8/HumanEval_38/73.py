### Encode and Decode Cyclic String Script
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
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
    
    :param s: The input string to be decoded.
    :return: The decoded string.
    """
    # Initialize an empty string to store the decoded result
    decoded_str = ""
    # Initialize a counter to keep track of the current index
    i = 0
    # Loop until we've processed the entire string
    while i < len(s):
        # Get the next group of three characters
        group = s[i:i+3]
        # If the group has only one character, just append it to the decoded string
        if len(group) == 1:
            decoded_str += group
            # Move the index 1 step forward
            i += 1
        # If the group has two characters, append them in reverse order
        elif len(group) == 2:
            decoded_str += group[1] + group[0]
            # Move the index 2 steps forward
            i += 2
        # If the group has three characters, cycle them as in encode_cyclic function
        else:
            decoded_str += group[1:] + group[0]
            # Move the index 3 steps forward
            i += 3
    return decoded_str


# Example usage
if __name__ == "__main__":
    s = "abcdefgh"
    encoded = encode_cyclic(s)
    decoded = decode_cyclic(encoded)
    print(f"Original string: {s}")
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")
```

This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. The example usage at the end demonstrates how to use these functions to encode and decode a string.