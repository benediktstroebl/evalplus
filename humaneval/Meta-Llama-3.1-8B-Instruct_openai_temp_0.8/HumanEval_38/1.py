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
    
    :param s: Input encoded string.
    :return: Decoded string.
    """
    # Initialize an empty string to store decoded result
    decoded = ""
    # Initialize an index to keep track of current character in string
    index = 0
    # Iterate over the encoded string
    while index < len(s):
        # If there are at least 3 characters remaining in the string
        if index + 3 <= len(s):
            # If the first character of the group is the same as the last character
            if s[index] == s[index + 2]:
                # Remove the last character from the group
                decoded += s[index + 1]
                # Move index 3 characters ahead
                index += 3
            else:
                # Otherwise, add all characters of the group to the decoded string
                decoded += s[index:index + 3]
                # Move index 3 characters ahead
                index += 3
        else:
            # If there are less than 3 characters remaining in the string
            # Add all remaining characters to the decoded string
            decoded += s[index:]
            # Break the loop
            break
    return decoded


# Test the functions
s = "HelloWorld"
encoded = encode_cyclic(s)
print(f"Encoded: {encoded}")
decoded = decode_cyclic(encoded)
print(f"Decoded: {decoded}")
```
This script defines two functions, `encode_cyclic` and `decode_cyclic`, to perform cyclic encoding and decoding on a string. The `encode_cyclic` function splits the input string into groups of three characters, and then cycles the elements in each group. The `decode_cyclic` function reverses this process by detecting and removing the cyclic elements from the encoded string.