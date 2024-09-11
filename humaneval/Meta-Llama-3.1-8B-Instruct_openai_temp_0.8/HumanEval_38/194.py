Here is the completed Python script that solves the problem:
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
    # Separate groups of 3 characters and groups with fewer characters
    groups = [(s[i:i+3], s[i+3:i+6]) for i in range(0, len(s), 6)]
    # Split each group into two substrings: cycled part and uncycled part
    groups = [group[0] + group[1][1:] + group[1][0] if len(group[0]) == 3 and len(group[1]) == 3 else group for group in groups]
    # Join all groups into one string
    return "".join(groups)


def main():
    # Example usage:
    original_str = "abcdefghijklmnopqrstuvwxyz"
    encoded_str = encode_cyclic(original_str)
    print(f"Original string: {original_str}")
    print(f"Encoded string: {encoded_str}")
    decoded_str = decode_cyclic(encoded_str)
    print(f"Decoded string: {decoded_str}")


if __name__ == "__main__":
    main()
```
In this script, the `encode_cyclic` function works as described in the problem statement. The `decode_cyclic` function splits the encoded string into groups of 3 characters and then decodes each group by cycling the elements. The `main` function demonstrates how to use these functions with an example string.