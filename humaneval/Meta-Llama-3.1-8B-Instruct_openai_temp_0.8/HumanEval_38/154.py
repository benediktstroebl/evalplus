Here is the completed Python script with the `decode_cyclic` function implemented:
```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Example usage:
if __name__ == "__main__":
    encoded_str = encode_cyclic("abcdef")
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")
```
The `decode_cyclic` function reverses the cycling process by prepending the last character of each group to the rest of the group. This effectively "cancels out" the cycling operation performed by `encode_cyclic`.