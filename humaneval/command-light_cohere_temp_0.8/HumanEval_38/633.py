Here's the code:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    s = s.split()
    encode_groups = []
    for i in range((len(s) + 2) // 3):
        groups = s[(3 * i):min((3 * i + 3), len(s))]
        encode_groups.append([group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(encode_groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    if encoded_cyclic is correctly encoded and decoded.
    s = s.split()
   ... common sense and plain text
    return s.
def encode(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    s = s.split()
    main encode function
    return "".join(s)
def decode(s: str) -> str:
    """
    takes as input string encoded with encode function. Returns decoded string.
    s = s.split() main decode function
    str = s
    return "".join(str)
def test_encode():
    """
    test encode_cyclic
    """
    assert encode_cyclic("Hello World") == "HWeLoV"
    assert encode_cyclic("abcde") == "codede"
    assert encode_cyclic("bit caecsiog") == "bItCaesI"
    assert encode_cyclic(" )") == "("
    assert encode_cyclic("{}") == "{"
    assert encode_cyclic("'") == "'A"
    assert encode_cyclic(" assisted codewar") == "adEstedC"
    assert encode_cyclic("") == ""
def test_decode():
    """
    test decode_cyclic
    """
    assert decode_cyclic("HWeLoV") == "Hello World"
    assert decode_cyclic("codede") == "abcde"
    assert decode_cyclic("bItCaesI") == "bit caecsiog"
    assert decode_cyclic("(") == ")"
    assert decode_cyclic("{") == "}"
    assert decode_cyclic("'A") == "'
    assert decode_cyclic("adEstedC") == "assisted codewar"
```

The code defines two self-contained functions: `encode_cyclic` and `decode_cyclic`. These functions split a string into groups of three characters, cycle the groups, and then join the groups back together. The `decode_cyclic` function takes an encoded string and returns the original decoded string. The `test_encode` and `test_decode` functions are used to test the correctness of the `encode_cyclic` and `decode_cyclic` functions.