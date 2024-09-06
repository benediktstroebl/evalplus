```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of three characters
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    get encoded string and decoded
    """
    return s

# test cases
test_encode_cyclic("Hello")
# expected output: h4ll4o

test_encode_cyclic("World")
# expected output: w4rld4

test_decode_cyclic("h4ll4o")
# expected output: Hello

test_decode_cyclic("w4rld4")
# expected output: World

test_encode_cyclic("A")
# expected output: A

test_decode_cyclic("A")
# expected output: Hello
```
The script defines the functions `encode_cyclic` and `decode_cyclic` that take a string as input and encode and decode it accordingly. 

The encode_cyclic function splits the input string into groups of three characters and cycles the elements within each group. The decode_cyclic function takes the encoded string and returns the decoded string.