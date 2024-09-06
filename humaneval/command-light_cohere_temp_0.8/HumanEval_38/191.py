```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return ["".join(group) for group in [group[1:] + group[0]) if len(group) == 3 else group for group in s.split(s, 3)]

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    returns decoded string
    """
    return "".join(group for group in encode_cyclic(s))

def test_encode_cyclic():
    """
    test string
    """
    assert encode_cyclic("abc").equals("".join(["".join([c, "d", "e"] + [c]))
    assert encode_cyclic("bed").equals("".join(["".join([c, "be"] + [c]))
    assert encode_cyclic("bdfe").equals("".join(["".join([c, "def"] + [c]))
    assert encode_cyclic("bedf").equals("".join(["".join([c, "bed"] + [c]))

def test_decode_cyclic():
    """
    test encode_cyclic and decode_cyclic function
    """
    assert decode_cyclic(encode_cyclic("")) == ""
    assert decode_cyclic("".join([c, "bc", "a"])) == "abc"
    assert decode_cyclic("".join([c, "bd", "ef"])) == "bedf"
    assert decode_cyclic("".join([c, "b", "ace"])).equals("".join([c,d, e, a]))

# run all the tests
test_encode_cyclic()
test_decode_cyclic()

I hope you enjoyed the self-contained solution.  It can also provide any other solutions or discuss different approaches to solving this problem.