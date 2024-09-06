```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    providing test string encoded by encode_cyclic function
    """
    return s.encode_cyclic()

# test cases
assertEqual(encode_cyclic("hello"),"    # ['hlroo'])
assertEqual(encode_cyclic("world"),"   # ['dlrow , dwolo'])
assertEqual(encode_cyclic("hello world"), # ['elroo , dllro , ello ,dlro'])
assertEqual(decode_cyclic("hello"),    # hello
assertEqual(decode_cyclic("dlrow"),    # hello )
assertEqual(decode_cyclic("hello world"), # hello world
```
This code defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function splits the input string into groups of three characters each, then cycles the characters in each group. The `decode_cyclic` function then takes the encoded string as input and returns the decoded string by passing it through `encode_cyclic`. The test cases ensure that the functions are working correctly by checking the output against the expected decoded string for various input strings.