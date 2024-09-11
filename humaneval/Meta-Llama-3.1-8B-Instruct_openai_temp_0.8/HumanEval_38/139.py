### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded.
    :return: Encoded string.
    """
    # Split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    :param s: Input string to be decoded.
    :return: Decoded string.
    """
    # Initialize decoded string
    decoded = ""
    # Initialize group index
    group_index = 0
    # Initialize character index
    char_index = 0
    
    # Loop through input string
    while char_index < len(s):
        # Get the current group
        group = s[group_index * 3:group_index * 3 + 3]
        # If group has fewer elements than 3, treat it as a group of its length
        group = group[:len(group) // 2] + group[len(group) % 2:]
        # Add characters from group to decoded string
        decoded += group
        # Move to the next group
        group_index += 1
        # Move to the next character
        char_index += 3
    
    return decoded


# Example usage
if __name__ == "__main__":
    original_string = "HelloWorld"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
This script provides functions for encoding and decoding a string using the cyclic encoding scheme. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and joins the groups back into a string. The `decode_cyclic` function reverses this process by splitting the input string into groups, identifying the group size from the number of characters in each group, and joining the characters back into a string. The script includes an example usage at the end to demonstrate how to use these functions.