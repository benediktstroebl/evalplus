### Cyclic Encoding and Decoding Script

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
    # Join groups to form encoded string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    # Initialize an empty string to store the decoded result
    decoded_str = ""
    # Initialize an index to track the current position in the string
    index = 0
    # Loop until the end of the string is reached
    while index < len(s):
        # Extract a group of three characters. If the remaining characters are less than 3, 
        # extract all remaining characters.
        group = s[index:index+3]
        # Cycle elements in the group by appending the first character to the end of the group
        # if the group has three characters.
        if len(group) == 3:
            group = group[1:] + group[0]
        # Append the decoded group to the decoded string and move the index three positions forward
        decoded_str += group
        index += 3
    return decoded_str


# Example usage:
if __name__ == "__main__":
    input_str = "abcdefgh"
    encoded_str = encode_cyclic(input_str)
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
    
    if input_str == decoded_str:
        print("Encoding and decoding process successful.")
    else:
        print("Error: Encoding and decoding process failed.")
```