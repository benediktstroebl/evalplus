### Cyclic Encoding and Decoding in Python
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Groups of three characters are formed from the input string. 
    In each group, the last character is moved to the beginning, 
    resulting in a cyclic shift. If a group has fewer than three characters, 
    it remains unchanged.
    
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
    Takes as input string encoded with encode_cyclic function. 
    Returns decoded string.
    
    This function reverses the encoding process by shifting each group 
    back to its original position.
    
    Args:
        s (str): The encoded string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # Initialize an empty string to store the decoded result
    decoded_string = ""
    
    # Initialize an index to track the current position in the string
    index = 0
    
    # Iterate over the encoded string
    while index < len(s):
        # Calculate the length of the current group
        group_length = min(3, len(s) - index)
        
        # Extract the current group
        group = s[index:index + group_length]
        
        # Shift the group back to its original position
        decoded_string += group[-1] + group[:-1]
        
        # Move the index to the next group
        index += group_length
    
    return decoded_string


# Example usage:
if __name__ == "__main__":
    original_string = "abcdefghij"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
    
    # Check if the decoded string matches the original string
    assert decoded_string == original_string, "Decoding failed"
    print("Decoding successful")
```
This script defines the `encode_cyclic` and `decode_cyclic` functions, which implement the cyclic encoding and decoding logic. The `encode_cyclic` function splits the input string into groups of three characters, cycles each group, and returns the encoded string. The `decode_cyclic` function reverses the encoding process by shifting each group back to its original position. The example usage demonstrates how to use these functions with an original string and verifies that the decoding process produces the original string.