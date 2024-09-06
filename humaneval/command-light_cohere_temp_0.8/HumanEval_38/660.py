```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    if the group has fewer than three characters, it is left as it is.
    otherwise it is the elements in the group by concatenating the first character
    and repeating the remaining two characters, then returning the string
    as a list of characters.
    """
    test_ the test_encode_cyclic("hello")
    assert encode_cyclic("hello") == "****"
    assert encode_cyclic("ooooooo") == "oooooooo"
    assert encode_cyclic("hellooo") == "oooooooo"
    assert encode_cyclic("abc") == "****"
    assert encode_cyclic("oi69") == "oi**o"
    assert encode_cyclic("bcc") == "bcc****"
    assert encode_cyclic("ggggg") == "ggg**g"
    assert encode_cyclic("hello world") == "****o**o**w"
    assert encode_cyclic("   ") == "****"
    assert encode_cyclic(" " ) == "****"
    assert encode_cyclic("123") == "****"
    assert encode_cyclic("abc123") == "****abc"
    assert encode_cyclic("") == "****"
    assert encode_cyclic([]) == "****"
    assert encode_cyclic({}) == "****"
    assert encode_cyclic([]) == "****"
    assert encode_cyclic({a: b}) == "****{b}****"
    assert encode_cyclic([a=b]) == "****{b}****"
    assert encode_cyclic({b: a}) == "****{a}****"
    assert encode_cyclic({a: [b=c]}) == "****{a}****{c}"
    assert encode_cyclic({a: {b: c}}) == "****{a}****{c}"
    assert encode_cyclic({b: {c: d}}) == "****{b}****{d}"
    return "ready"

def decode_cyclic(s: str) -> None:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    test test_
```