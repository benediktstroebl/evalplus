```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    specific case:
    - encoded string must be the output of encode_cyclic.
    - input string must match the string that encode_cyclic returns.
    """
    method should return the same string decoded with encode_cyclic.
    """
output:
    decoded string

test case 1:
    ".........xx"(should return ".........xx")

test case 2:
    "....xx.....x"(should return "....xx..x")

test case 3:
    "x.....xx...x"(should return "x.....xx")

test case 4:
    "abc..."abc"(should return "abc"abc")

test case 5:
    "a...bb..."abc"(should return "........ab")

test case 6:
    "...aabb".joinabc"(should return "....abc")

test case 7:
    "abcdefghijklmnopqr..."abcdefghijklmnopqr"(should return "abcdefghijklmnopqr")

test case 8:
    "....# 123456"#abc"(should return "....# 123456abc")

test case 9:
    "abcdefghijklmnopQRSTUV"#abcdefghijklmnopQRSTUV"(should return "abcdefghijklopQRSTUV")

test case 10:
    "aaaaaa".aaaaaaa"(should return "....".aaaaaa).