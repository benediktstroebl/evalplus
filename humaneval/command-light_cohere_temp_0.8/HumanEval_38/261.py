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
    recorder strs
 def rec(s):
        if not recs:
            rec_ = [s[i:i + 3] for i in range(0, len(s) - 2)]
            return rec
    return "".join(rec)

# encode and decode test cases
print(encode_cyclic("abc")) # deque
print(encode_cyclic("abcd")) # deque
print(encode_cyclic("abcdef")) # deque
print(decode_cyclic("defg")) # "abcdefg")
print(decode_cyclic("fehrts"))) # "abcdefghij"
```
This Python script defines a self-contained function to encode and decode strings using a cyclic encoding technique. It utilizes two functions: `encode_cyclic` and `decode_cyclic`. The encode function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function, on the other hand, takes an encoded string as input and returns the decoded string. It uses a recorder objects to store the encoded string in groups of three characters, and then returns the decoded string by unpicking the elements from these groups. 

Finally, the script provides a series of test cases to demonstrate the functionality of the functions. The output will display the expected decoded strings.