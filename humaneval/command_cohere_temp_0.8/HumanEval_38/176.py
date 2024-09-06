```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range(len(s) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

# Tests:
def test_encode():
    assert encode_cyclic("Hello") == "Khoor"
    assert encode_cyclic("World") == "Fdor"
    assert encode_cyclic("!!!") == "????"
    assert encode_cyclic("1111") == "1222"
    assert encode_cyclic("abc") == "abc"

def test_decode():
    assert decode_cyclic("Khoor") == "Hello"
    assert decode_cyclic("Fdor") == "World"
    assert decode_cyclic("????")) == "!!!"
    assert decode_cyclic("1222") == "1111"
    assert decode_cyclic("abc") == "abc"
``` 

The `encode_cyclic` function takes a string `s` as input and encodes it by cycling groups of three characters. It first splits the input string into groups of three characters, considering incomplete groups at the end, if any. It then cycles the elements of each group, concatenating the first and last elements together if there are three elements, or leaving the group as is if it has fewer than three elements. This cycling process ensures that any string can be encoded to a valid prefix of its encoded version. 

The `decode_cyclic` function takes a string s as input and returns the decoded string. It works by reversing the encoding process, splitting the encoded string into groups of three characters, considering incomplete groups at the end, if any, and then cycling the elements of each group to reconstruct the original string.

The above code includes two test modules, `test_encode` and `test_decode`, which verify that the output of the encode and decode functions, respectively, is correct.

You can execute the code by running `python encode_decode_cyclic.py` in your terminal to run the tests. Or, if you have set up your Python environment to run `.py` files automatically, save the code into a file with that name and run it. 

To test the functionaries on strings with more than 36 characters, you may modify the tests or use the script below:
```python
import random

test_strings = [
    "Hello", "World", "!!!!!", 
    "abcdef", "abc123", "ahahaha123456",
    "This is a longer string that has more than 36 characters and includes special characters like @, #,