```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = [['...'] for _ in range(len(s) + 2) // 3]]
    for i in range((len(s) + 2) // 3):
        groups[i // 3 * 3] = s[i:min((i + 3), len(s))]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    example:
    Test string for decode_cyclic function
    s = '<...>'
    assert decode_cyclic(s) == '<...>'
    s = '....xx.'
    assert decode_cyclic(s) == '....x'
    s = '....xx..xx'
    assert decode_cyclic(s) == '....x..x'
    s = 'xx.xxxx.xx xx'xx.' stir tomorrow.'.xxx.sh'
   Guards wells x possible
```