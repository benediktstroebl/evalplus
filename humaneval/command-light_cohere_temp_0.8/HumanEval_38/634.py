```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    time split between encoded and decoded string.
    return s.decode_unicode("".
    / encode_cyclic(s))

tests = [
    s = "abcd".encode_cyclic(s)
    assert s == "bcaca"
   
    s = "xyzz".encode_cyclic(s)
    assert s == "yzzzzz"
   
    s = "aaaa".encode_cyclic(s)
    assert s == "aaaaa"
   
    s = "afd".encode_cyclic(s)
    assert s == "dfaafd"
   
    s = "ab".encode_cyclic(s)
    assert s == "baba"
    s = "aefgbeif".decode_cyclic(s)
    assert s == "abcdefghijklmnopqr"
    ```