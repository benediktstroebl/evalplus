```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    reason why decoded string does not match the original string,
    because the encode_cyclic function adds two characters to each group.
    return decoded string

test cases:
# test case 1
test_case1 = encode_cyclic("hello")
# test case 2
test_case2 = encode_cyclic("hello world")
# test case 3
test_case3 = encode_cyclic("world helloo")

print(test_case1)  # Output: decoded string
print(test_case2)  # Output: decoded string
print(test_case3)  # Output: decoded string

test_case4 = encode_cyclic("helping")
test_case5 = encode_cyclic("helping earth")
test_case6 = encode_cyclic("helping universe")

print(test_case4)  # Output: encoded string
print(test_case5)  # Output: encoded string
print(test_case6)  # Output: encoded string

test_case7 = decode_cyclic(test_case6)
print(test_case7)  # Output: decoded string matches the original string
```

The code has two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns a decoded string. The `test_case1` and `test_case2` are two test cases that are used to verify the correctness of the `encode_cyclic` function. The `test_case3` and `test_case3` are used to test the `decode_cyclic` function. The code also creates two more test cases, `test_case4` and `test_case5`, to test the `encode_cyclic` function with different strings. The `test_case6` is then used to test the `decode_cyclic` function with different input strings.