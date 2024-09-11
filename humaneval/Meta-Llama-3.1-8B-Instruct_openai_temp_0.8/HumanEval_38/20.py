### Cyclic Encoding and Decoding Script
```python
def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of three characters.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group, unless the group has fewer elements than 3
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
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
    decoded = ""
    
    # Initialize an empty temporary string to store the current group
    temp_group = ""
    
    # Iterate through each character in the encoded string
    for char in s:
        # Add the character to the current group
        temp_group += char
        
        # If the length of the group is 3, add it to the decoded string and reset the group
        if len(temp_group) == 3:
            # If the group has fewer elements than 3, we don't cycle elements
            if len(temp_group) < 3:
                decoded += temp_group
            else:
                # Cycle the elements in the group
                decoded += temp_group[1:] + temp_group[0]
            temp_group = ""
    
    # Add any remaining characters in the group to the decoded string
    if temp_group:
        # If the group has fewer elements than 3, we don't cycle elements
        if len(temp_group) < 3:
            decoded += temp_group
        else:
            decoded += temp_group[1:] + temp_group[0]
    
    return decoded


# Example usage:
if __name__ == "__main__":
    # Test encoding and decoding
    original_string = "abcdefghijklmnopqrstuvwxyz"
    encoded_string = encode_cyclic(original_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
    
    # Check if the original and decoded strings match
    if decoded_string == original_string:
        print("Encoding and decoding is successful!")
    else:
        print("Error: Encoding and decoding is not successful.")
```
This script includes both the `encode_cyclic` and `decode_cyclic` functions, along with example usage to test their functionality.