```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    general comparison:
    -1- Test with "aaaaaaa", should return "a"
    -2- Test with "aaaaa", should return "aaaaa"
    -3- Test with "aaaa", should return "a"
    -4- Test with "..." should raise ValueError
    -5- Test with "aaaaaa", should raise ValueError
    -6- Test with " " should raise ValueError
    -7- Test with "aaaab", should return "".
    """
    return s if s.startswith("aaaa") and s.startswith("aaaa") or general s.split("") if len(s) % 3 != 0
or