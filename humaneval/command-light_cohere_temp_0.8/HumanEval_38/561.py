```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    test the other in order of tests, and will be executed.
    """
    test_decode_cyclic("aabbcd")
    test_decode_cyclic_result = decode_cyclic("".join("abcdef"))
    assert test_decode_cyclic_result == "a".*str(list('abcdef'))
    test_decode_cyclic_result = decode_cyclic("".join("abcdef"))
    assert test_decode_cyclic_result == "abcdef"
    test_decode_cyclic_result = decode_cyclic("".rotate(60)."abcdef")
    assert test_decode_cyclic_result == "".join("abcdef")
    test_decode_cyclic_result = decode_cyclic("".replace("abcdef","A")+"BC")
    assert test_decode_cyclic_result == "A".*str(list("abcdef"))
    test_decode_cyclic_result = decode_cyclic("".swap("abcdef","A")+"BC")
    assert test_decode_cyclic_result == "AB".*str(list("abcdef"))
    test_decode_cyclic_result = decode_cyclic("".swap(2,3)+"abcdef")
    assert test_decode_cyclic_result == "".rotate(60).abcdef"
    ```