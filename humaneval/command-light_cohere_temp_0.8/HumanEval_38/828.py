Here is a Python script that has a self-contained function that solves the problem you've described:

```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    strategy: decode the string in the reverse order
    groups = [g for g in s.decode_cyclic(groups)[::-1]]
    return "".join(groups)

# test cases
test_str = "abc#bcd"
test_decoded = decode_cyclic(test_str)
print("Test decoded:", test_decoded)

test_str = "abc#cd#abc"
test_decoded = decode_cyclic(test_str)
print("Test decoded:", test_decoded)

test_str = "abc# #abc"
test_decoded = decode_cyclic(test_str)
print("Test decoded:", test_decoded)
``` 
This script provides a self-contained solution and test cases for the given problem.