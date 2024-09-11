```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    # Split the string into groups of three characters, padding with empty strings if necessary
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle the elements in each group, unless the group has fewer than three elements
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups into a single string
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Decodes a string encoded with the encode_cyclic function.
    
    Args:
        s (str): The encoded string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # Initialize an empty string to store the decoded result
    decoded_string = ""
    
    # Initialize an index to track the current position in the encoded string
    i = 0
    
    # Iterate over the characters in the encoded string
    while i < len(s):
        # If the current character and the next two characters form a group of three, shift them
        if i + 2 < len(s):
            # Store the current character to be shifted to the end
            shift_char = s[i]
            # Shift the group of three characters
            group = s[i+1:i+4]
            # Add the shifted group to the decoded string
            decoded_string += group[1:] + group[0]
            # Add the shifted character to the decoded string
            decoded_string += shift_char
            # Move the index three positions forward
            i += 3
        # If the current character is the only character in the remaining part of the encoded string, add it to the decoded string as is
        else:
            decoded_string += s[i]
            i += 1
    
    # Return the decoded string
    return decoded_string


# Example usage:
if __name__ == "__main__":
    encoded_string = encode_cyclic("abcdefg")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script defines two functions, `encode_cyclic` and `decode_cyclic`, for encoding and decoding strings using the cyclic shift method. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group unless the group has fewer than three elements, and returns the encoded string. The `decode_cyclic` function reverses the process by shifting the elements in each group back to their original positions. The example usage at the end demonstrates how to use these functions.