```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group, unless the group has fewer than 3 characters
    return ''.join(groups) if len(groups) >= 3 else ''.join(groups)

    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    """
    # Convert to lowercase to match the uppercase values in the encode_cyclic
    # function.
    s = s.lower()

    y = s.split()
    example
    str = ""
    for i in range(len(y) - 2):
        str += y[i] + y[i + 1]
    return str.dec()

tests = [
    'hellow world',
    'hello world',
    'wor lllod',
    'hello world 123',
    'abc123 def456',
    'This is the test',
    'this is a test 123',
    ''.join(encode_cyclic, "hello world"),
    'hello world'.decode_cyclic()
]

print(tests[0] == tests[-1]) 
``` 

This Python code defines two functions, `encode_cyclic` and `decode_cyclic`, for encoding and decoding a string using a cyclic encoding technique. The `encode_cyclic` function splits the input string into substrings of length 3, then cycles through these groups, encoding the characters by capitalizing them and appending the results to a new string. The `decode_cyclic` function does the reverse, decoding the input string by splitting it into substrings and then cycling through the characters in each group to get the original string.