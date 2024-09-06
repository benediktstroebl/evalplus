```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    provided that tests.
    test encode_cyclic('hello')
    assert encode_cyclic('hello') == 'hcsdol'
    test encode_cyclic('world')
    assert encode_cyclic('world') == 'ldow'
    test encode_cyclic('abcdeabcde')
    assert encode_cyclic('abcdeabcde') == 'ecdvagcde'
    test encode_cyclic('abc...abc')
    assert encode_cyclic('abc...abc') == 'a...cba'
    test encode_cyclic('')
    assert encode_cyclic('') == ''
    test encode_cyclic('abc')
    assert encode_cyclic('abc') == 'abc'
    test encode_cyclic('A')
    assert encode_cyclic('A') == 'aa'
    test encode_cyclic('360')
    assert encode_cyclic('360') == 'u'
    test encode_cyclic('aab')
    assert encode_cyclic('aab') == 'abab'
    test decode_cyclic('hcsdol')
    assert decode_cyclic('hcsdol') == 'hello'
    test decode_cyclic('ldow')
    assert decode_cyclic('ldow') == 'world'
    test decode_cyclic('ecdvagcde')
    assert decode_cyclic('ecdvagcde') == 'abcdeabcde'
    test decode_cyclic('a...cba')
    assert decode_cyclic('a...cba') == 'abc...abc'
    test decode_cyclic('')
    assert decode_cyclic('') == ''
    test decode_cyclic('abc')
    assert decode_cyclic('abc') == 'abc'
    test decode_cyclic('A')
    assert decode_cyclic('A') == 'A'
    test decode_cyclic('360')
    assert decode_cyclic('360') == '360'
    test decode_cyclic('u')
    assert decode_cyclic('u') == 'aab'
    ```