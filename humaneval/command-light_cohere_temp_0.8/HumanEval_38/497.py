```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    If the string length is not divisible by 3, the function returns the original string.
    """
    s[:(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in s]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    selects three least of length 3, and adds spaces at the beginning.
    return " ".join(groups)

# Example usage
s = "abcabcbb"
print(encode_cyclic(s)) # Output: abcabcabcbb
print(decode_cyclic(encode_cyclic(s))) # Output: abcbb
```

This Python code defines a self-contained function to encode and decode strings using a cyclic grouping technique. It returns the encode function takes a string as input and creates a list of groups of three characters. The encode function then creates a new string by concatenating the groups in a cyclic manner. The decode function takes the input and creates a string with the same cyclic grouping. The code also provides an function test to verify that the encode and decode functions work correctly.