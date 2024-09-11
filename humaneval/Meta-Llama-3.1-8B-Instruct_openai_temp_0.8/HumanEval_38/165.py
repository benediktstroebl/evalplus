### Cyclic Encoding and Decoding in Python
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
    # Initialize an empty list to store decoded groups
    decoded_groups = []
    
    # Initialize an empty string to store current group
    current_group = ""
    
    # Iterate over the encoded string
    for char in s:
        # Add character to the current group
        current_group += char
        
        # If the current group has 3 characters, add it to the decoded groups list and reset the current group
        if len(current_group) == 3:
            # If the current group has 3 characters, cycle them
            if len(current_group) == 3:
                decoded_groups.append(current_group[1:] + current_group[0])
            else:
                decoded_groups.append(current_group)
            current_group = ""
    
    # Add the last group to the decoded groups list if it's not empty
    if current_group:
        # If the current group has 3 characters, cycle them
        if len(current_group) == 3:
            decoded_groups.append(current_group[1:] + current_group[0])
        else:
            decoded_groups.append(current_group)
    
    # Join the decoded groups into a single string
    return "".join(decoded_groups)


def test_cyclic_encoding_and_decoding():
    # Test the functions
    test_string = "abcdef"
    encoded_string = encode_cyclic(test_string)
    decoded_string = decode_cyclic(encoded_string)
    
    assert decoded_string == test_string, f"Expected {test_string}, got {decoded_string}"
    
    print("Tests passed!")


if __name__ == "__main__":
    test_cyclic_encoding_and_decoding()
```
This script first defines the `encode_cyclic` function, which takes a string `s` as input, splits it into groups of three characters, and cycles the elements in each group. The `decode_cyclic` function takes an encoded string as input, splits it into groups, and cycles the elements in each group to reconstruct the original string. The `test_cyclic_encoding_and_decoding` function tests the `encode_cyclic` and `decode_cyclic` functions by encoding a test string, decoding the encoded string, and asserting that the decoded string is equal to the original test string. If the test passes, it prints "Tests passed!".