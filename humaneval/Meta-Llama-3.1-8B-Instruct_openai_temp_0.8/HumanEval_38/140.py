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
    if not s or len(s) % 3!= 0:
        raise ValueError("Input string must have a length that is a multiple of 3")

    decoded_groups = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:  # if group has 3 elements
            decoded_groups.append(group[1:] + group[0])  # cycle elements
        else:  # if group has fewer than 3 elements
            decoded_groups.append(group)  # just append group

    return "".join(decoded_groups)


# Example usage:
encoded_str = encode_cyclic("abcdefgh")
decoded_str = decode_cyclic(encoded_str)

print(f"Encoded string: {encoded_str}")
print(f"Decoded string: {decoded_str}")
```

This script implements the `encode_cyclic` and `decode_cyclic` functions as specified. In the `decode_cyclic` function, we have added a check at the beginning to ensure the input string has a length that is a multiple of 3, as the `encode_cyclic` function would not be able to handle strings with lengths that are not multiples of 3. If such an input string is passed to the `decode_cyclic` function, it raises a ValueError with a corresponding message. 

In the example usage, we are encoding the string `"abcdefgh"` using the `encode_cyclic` function and then decoding the result using the `decode_cyclic` function. The encoded and decoded strings are then printed to the console.