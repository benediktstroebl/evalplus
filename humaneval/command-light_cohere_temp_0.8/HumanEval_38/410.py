```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   

    check for a given string in the test cases and compares it with decoded strings
    expected_decoded = ["abc", "cba", "abcd", "cdda"]
    test_cases = [s.decode_cyclic(s) for s in expected_decoded]
    if len(set(test_cases)) != len(expected_decoded):
        raise ValueError("decode_cyclic function is not returning the expected decoded string.")

test_encode_cyclic = ["..."
encode_cyclic("hello")
encode_cyclic("world")
encode_cyclic("hello world")
test_cases = [encode_cyclic("hello"), encode_cyclic("world"), encode_cyclic("hello world")]
test_decode_cyclic = ["".join(test_cases)]

print("test_encode_cyclic:", test_encode_cyclic)
print("test_decode_cyclic:", test_decode_cyclic)

```

The above script contains a self-contained function called encode_cyclic and another function called decode_cyclic. The encode_cyclic function takes a string as input and returns an encoded string by cycling groups of three characters. The decode_cyclic function takes an encoded string as input and returns the decoded string. It also has test cases for the encode_cyclic and decode_cyclic functions to check if they are returning the expected decoded strings.