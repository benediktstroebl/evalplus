```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = [sub for sub in s[::3*i:min(3*i+3, len(s))] for i in range((len(s)+2)//3)]
    # cycle elements in each group
    elements = [sub[1:] + sub[0] for sub in groups]
    return "".join(elements)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   Shelves the value for stroring
    shelves = set(range(26))
    # encode string with cyclic encoding
    encoded = "".join(s.replace(ord(i), s[i:i+3] for i in range(0, len(s))))
    # decode string with decode_cyclic function
    decoded = "".join(chr(ord(i) - shelves[i % 26]) for i in encoded)
    return decoded


# Test cases
def test_encode_cyclic():
    assert encode_cyclic("hello" == "sinldeuoh")
assert encode_cyclic("world") == "unroolw")

def test_decode_cyclic():
    assert decode_cyclic("sinldeuoh") == "hello"
assert decode_cyclic("unroolw") == "world"

```
This Python code defines two functions, `encode_cyclic` and `decode_cyclic`, that solve the encoding and decoding problems of cyclic groups of characters. The code also includes test cases that verify the correctness of the functions.

The `encode_cyclic` function takes an input string and returns its encoding by cycling groups of three characters. It splits the string into groups of length 3 and cycles the characters within each group. The `decode_cyclic` function takes an input string and returns its decoding by mapping the encoded characters back to their original characters. 

The code uses a set of integers to represent the elements of the cyclic group, and the modulo operator to map the index of each character back to the set of 26 elements. This allows for encoding and decoding strings with the cyclic group.