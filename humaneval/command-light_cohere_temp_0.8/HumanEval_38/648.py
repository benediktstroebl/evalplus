Here is a Python script that includes the self-contained function `encode_cyclic` and its associated tests:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def test_encode_cyclic():
    """
    test string
    """
    assert encode_cyclic("hello world") == "hed..."
    assert encode_cyclic("hello World") == "elow orenld"
    assert encode_cyclic("hello, world") == "elod envw"
    assert encode_cyclic("hello , World!alow,rold") == "aelod vrened"
    assert encode_cyclic("hello, abc123") == "hed olec123"
    assert encode_cyclic("") == ""

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
!