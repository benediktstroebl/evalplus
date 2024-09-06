```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    local test cases.
    """
    test encode_cyclic('hello')
    assert encode_cyclic('hello') == '🟨hollolooo'
    # test decode_cyclic
    assert decode_cyclic('🟨hollolooo') == 'hello'
    assert decode_cyclic('⅟×⅟⅟×Ⅳ⅟⅂') == 'abc'
    assert decode_cyclic('😂🦴🧘') == 'cute alien'
    assert decode_cyclic('🔊💡🎌