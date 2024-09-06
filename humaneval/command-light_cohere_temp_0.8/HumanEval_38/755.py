```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    formed by the of encoded groups.
    """
    (no) values should be escaped.
    """

This is a test string: "ayay..."

assert encode_cyclic("...ay") == "....#"; # Test 1

assert encode_cyclic("...") == "..."  # Test 2

assert encode_cyclic("...") == "..#"  # Test 3

assert encode_cyclic("#") == "##"  # Test 4

assert encode_cyclic("...") == "..."  # Test 5

assert encode_cyclic("aaaa") == "aa#..."  # Test 6

assert encode_cyclic("#aaaa") == "##aaaa"  # Test 7

assert encode_cyclic(" crazs ") == "caz##"  # Test 8

```