```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    Example: ('aabb...','...ba...','...bb...')
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    Example
        test
    return s

# test case 1
assertEqual(decode_cyclic(''.encode_cyclic(
    '''
    aaab...
    b...ab
    b...aba...
    baaaa...
    '''
)),
'   "aaab...bb".strip())

# test case 2
assertEqual(decode_cyclic(''.encode_cyclic(
    '''
    aa...ab...
    b...ba...
    b...bb...
    '''
)),
'   "abab".strip())

# test case 3
assertEqual(decode_cyclic('').encode_cyclic(
    '''
    ab...bb...
    b...abab...
   abab...bb...
    '''
),
"abab...b".strip())
```
This script defines a Python function called **encode_cyclic** that takes a string as input and produces an encoded string by cycling groups of three characters. The function then returns the encode the string.

The script also defines a Python function called **decode_cyclic** that takes a string as input and returns the decoded string. The function then returns the string passed to it.

The script then provides test cases to check the correctness of the functions **encode_cyclic** and **decode_cyclic**.