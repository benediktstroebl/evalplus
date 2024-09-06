Here's a Python script that solves the problem of encoding and decoding markdown code blocks using the `encode_cyclic` and `decode_cyclic` functions:

```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    

    # remove the line breaks and encode the content of the markdown block.
    """
    return "".join(decode(s, encoding='utf-8').encode(), encoding='utf-8'))

def test_encode_decode():
    """
    test the encode_cyclic and decode_cyclic functions
    """
    assert encode_cyclic("hello world") == "..."
    assert encode_cyclic("hello, world!") == "====-"
    assert encode_cyclic("hello\nworld") == "..."
    assert encode_cyclic("goodbye") == "..."
    assert encode_cyclic("\t\t\tThis is a test") == "..."
    assert encode_cyclic("----") == "..."
    assert encode_cyclic("---") == "---"
    assert encode_cyclic("..." + "\n") == "..." + "--"
    assert encode_cyclic("") == "..."
    assert encode_cyclic(" ")[1:] == " "
    assert encode_cyclic("\t") == " "
    assert encode_cyclic("\t\t") == " ,"
    assert encode_cyclic("\t\t\t") == " ,"
    assert encode_cyclic("hello world\nhello!") == "..." + "---"
    assert decode_cyclic("---") == "hello world\nhello!"
    assert decode_cyclic("---") == "\n"
    assert decode_cyclic("   ") == ""
    assert decode_cyclic("   ") == ""
    assert decode_cyclic("   ") == ""
    assert decode_cyclic("---\n---") == "hello world\nhello!"
```

This script defines a function `encode_cyclic` that takes a string as input and returns an encoded version of the string by cycling groups of three characters. The `decode_cyclic` function takes the encoded string as input and returns the decoded version of the string. The `test_encode_decode` function tests the `encode_cyclic` and `decode_cyclic` functions by passing various input strings and checking if the output is correct.