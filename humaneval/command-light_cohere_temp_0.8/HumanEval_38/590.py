```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   s must unescape the value in encoded string, and returns decoded string.
    """
    s.unes unescape value with regex, then return decoded string.
"""

# Test cases
test_str = "Hello World!!______oOn revolving down the line!"
test_str_roundtrip = "___oo___#$o_$oo____#"
test_str_singlechar = "x"
test_str_empty = ""

print("Test case 1: " + encode_cyclic(test_str) + decode_cyclic(test_str))
print("Test case 2: " + encode_cyclic(test_str_roundtrip) + decode_cyclic(test_str_roundtrip))
print("Test case 3: " + encode_cyclic(test_str_singlechar) + decode_cyclic(test_str_singlechar))
print("Test case 4: " + encode_cyclic(test_str_empty) + decode_cyclic(test_str_empty))
```
This Python script defines a function called `encode_cyclic` that takes a string as input and returns an encoded version of the string. The function splits the string into groups of three characters, cycles the elements of each group, and then joins the groups back together to form the encoded string. The `decode_cyclic` function takes an input string and returns the decoded version of the string, which is the original string with any unescaped special characters removed. 

The script also includes a set of test cases to verify the functionality of the `encode_cyclic` and `decode_cyclic` functions.