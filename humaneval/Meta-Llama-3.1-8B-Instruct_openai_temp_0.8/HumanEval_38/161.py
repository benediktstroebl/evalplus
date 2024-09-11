### Cyclic Encoding and Decoding
```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    
    :param s: Input string to be encoded.
    :return: Encoded string with cycled groups of three characters.
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
    result = ""
    i = 0
    while i < len(s):
        if i + 2 < len(s):
            # If we have a complete group of three characters, move two positions forward
            result += s[i:i+3][1] + s[i:i+3][0]
            i += 3
        else:
            # If we don't have a complete group of three characters, just append the remaining characters
            result += s[i:]
            break
    return result


# Example usage:
if __name__ == "__main__":
    input_string = "abcdefgh"
    encoded_string = encode_cyclic(input_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script provides two functions, `encode_cyclic` and `decode_cyclic`, to encode and decode strings by cycling groups of three characters. The `encode_cyclic` function splits the input string into groups of three characters and cycles them, unless the group has fewer elements than three. The `decode_cyclic` function reverses this process by identifying groups of three characters in the encoded string and moving two positions forward to extract the cycled character. The example usage at the end demonstrates how to use these functions to encode and decode a test string.