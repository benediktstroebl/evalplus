```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    Args:
        s (str): The input string to be encoded.
    
    Returns:
        str: The encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    
    Args:
        s (str): The input string to be decoded.
    
    Returns:
        str: The decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # if a group has fewer elements than 3, fill it with the last character of the previous group
    if len(groups) >= 2:
        for i in range(len(groups) - 1):
            if len(groups[i + 1]) <= 3:
                groups[i + 1] += groups[i][-1]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Test the functions
if __name__ == "__main__":
    test_string = "HelloWorld"
    encoded_string = encode_cyclic(test_string)
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
    assert test_string == decoded_string, f"Decoded string is incorrect, expected '{test_string}', got '{decoded_string}'"
    print("Tests passed.")
```

This script first defines the `encode_cyclic` function to cycle groups of three characters in the input string. The `decode_cyclic` function is then defined to reverse this process. In the `decode_cyclic` function, if a group has fewer elements than 3, it is filled with the last character of the previous group to ensure the decoding process is reversible. Finally, the script tests the functions with a sample input string.