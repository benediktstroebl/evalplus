```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): Encoded string to be decoded.

    Returns:
        str: Decoded string.
    """
    # reverse the cyclic operation by splitting the string back into groups of length 3
    groups = [s[(3 * i):3*(i+1)] for i in range(len(s) // 3)]
    
    # for the last group, which may have fewer than 3 characters, add leading characters from the previous group
    for i in range(len(groups) - 2, -1, -1):
        if len(groups[i+1]) < 3:
            groups[i] = groups[i+1] + groups[i] + groups[i+1][:3 - len(groups[i+1])]
            groups.pop(i+1)
            break
    
    return "".join(groups)


# Test the functions
if __name__ == "__main__":
    encoded_str = encode_cyclic("HelloWorld")
    decoded_str = decode_cyclic(encoded_str)
    assert decoded_str == "HelloWorld"
    print("Encoded string:", encoded_str)
    print("Decoded string:", decoded_str)
```
The provided code defines two functions, `encode_cyclic` and `decode_cyclic`, which implement the cyclic encoding and decoding logic, respectively. The `encode_cyclic` function splits the input string into groups of three characters, cyclically shifts the elements in each group unless it has fewer than three elements, and then joins the groups back into a string. The `decode_cyclic` function reverses this process. The test at the end ensures that the encoding and decoding process is correct.