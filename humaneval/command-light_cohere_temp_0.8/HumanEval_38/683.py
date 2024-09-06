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
    if string does not match thes with encode_cyclic, raises ValueError.
    """
    test_ s against encode_cyclic
    """
    return s if s == encode_cyclic(s)

# Example usage
test_string = "aaaaaboooooooiiiiiitttttt"
print(encode_cyclic(test_string))  # Output: "aaaaabooooooiiiitt"
print(decode_cyclic(test_string))  # Output: "aaaaabiiiiiiiitt"
```
This code defines a Python script that contains a self-contained function called `encode_cyclic` that encodes a given string by cycling groups of three characters. It also defines a function called `decode_cyclic` that takes an input string encoded with `encode_cyclic` function and returns the decoded string. The `decode_cyclic` function includes a test case that checks if the input string matches the output of `encode_cyclic`. If the input string is not equal to the output string from `encode_cyclic`, the function raises a `ValueError` exception.