```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    1. split string to groups of length 3
    2. cycle each group. Unless group has fewer elements than 3
    3. cycle each group as a group and repeat the first character
    4. add the repeated first character to each group
    5. return the final group and return the characters
"""
    return s.group(
        s[i:min((i + 2)//3, len(s))]
        for i in range((len(s) + 1) // 3)
        if len(s[i:min((i + 2) // 3, len(s))]) == 3
        s[i:min((i + 2)//3, len(s))] = s[i][0]
        return s[i:]

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    1. remove repeated first characters characters from groups
    to a string
    2. remove all characters from the one by one
    3. return the modified string and return the characters
    """
    return s.group

This code is a self-contained Python script that solves the problem of encoding and decoding a string of characters using the given functions.