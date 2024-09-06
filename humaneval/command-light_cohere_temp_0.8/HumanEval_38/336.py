```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3. Each of these groups contains a characters repeated once.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   gets in the expected encoded string by encode_cyclic function
    """
    return encode_cyclic(s) == s

# Test case 1: Encode "hello"
test_case1 = "hello"
encoded = encode_cyclic(test_case1)
assert encoded == "dhvvielyob"

# Test case 2: Encode "world"
test_case2 = "world"
encoded2 = encode_cyclic(test_case2)
assert encoded2 == "lwjdlro"

# Test case 3: Decode "dhvvielyob"
decoded = decode_cyclic("dhvvielyob")
assert decoded == "hello"

# Test case 4: Decode empty string
decoded4 = decode_cyclic("")
assert decoded4 == ""

# Test case 5: Decode "world"
decoded5 = decode_cyclic("lwjdlro")
assert decoded5 == "world"

print("All tests passed!")
```

This Python script defines a self-contained function `encode_cyclic` that takes a string as input and returns an encoded string by cycling groups of three characters. It also defines a `decode_cyclic` to decode the input string. The code also includes a set of test cases to verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.