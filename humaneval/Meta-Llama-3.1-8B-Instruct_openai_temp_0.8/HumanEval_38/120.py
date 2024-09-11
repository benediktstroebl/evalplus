Here's a self-contained Python script that solves the problem:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)


# Testing the functions
if __name__ == "__main__":
    encoded_string = encode_cyclic("Hello, World!")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_cyclic(encoded_string)
    print(f"Decoded string: {decoded_string}")
```
To run this script, save it to a file (e.g., `cyclic_encoding.py`) and run it with Python (e.g., `python cyclic_encoding.py`). You can replace `"Hello, World!"` with any string you'd like to encode and decode.