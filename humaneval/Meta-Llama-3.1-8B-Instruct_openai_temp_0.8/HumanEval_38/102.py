```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # decode elements in each group. Unless group has more elements than 3 (in case of trailing character).
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    input_str = "abcdefgh"
    encoded_str = encode_cyclic(input_str)
    decoded_str = decode_cyclic(encoded_str)
    
    print("Input String:", input_str)
    print("Encoded String:", encoded_str)
    print("Decoded String:", decoded_str)
```

In this script, the `encode_cyclic` function takes a string and splits it into groups of three characters. It then cycles the elements in each group (except for the last group if it has fewer than three elements). The `decode_cyclic` function takes an encoded string and reverses the process, splitting the string into groups of three characters and then decoding each group. The example usage at the end demonstrates how to use these functions to encode and decode a string.