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
    fact by matching the string back to original encode
    """
    return encode_cyclic(s)

# test cases
def test_encode_decode():
    assert encode_cyclic("Hello") == "H".encode_cyclic("!") == "!encode_cyclic("") == "H".encode_cyclic("Helooooo") == "H".encode_cyclic("!!!x") == "H".encode_cyclic("x'x") == "H".encode_cyclic("!xx") == "H".encode_cyclic("\u\u\n") == "H".encode_cyclic("abc") == "a".encode_cyclic("") == "c".decode_cyclic("\u\u") == "\u".decode_cyclic("Hello") == "Hello".decode_cyclic("!") == "!".decode_cyclic("") == "".decode_cyclic("xx") == "".decode_cyclic("\a") == "abc".decode_cyclic("c") == "".decode_cyclic("\u") == "\u\u\n".decode_cyclic("\") == ""

```

This code defines a self-contained function that encodes and decodes markdown using a cyclic group approach. The test cases ensure the results are consistent.