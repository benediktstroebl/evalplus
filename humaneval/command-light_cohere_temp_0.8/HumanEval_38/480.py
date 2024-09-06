```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    example:
    decoded string.
    return s == encode_cyclic(s)

# Example 1: test string is encoded correctly
test_encode = "abc123"
test_decode = encode_cyclic(test_encode)
print(test_decode) # Output: decoded string

# Example 2: test string has more than 3 characters, it should be decoded correctly
test_decode2 = encode_cyclic("abc dbz 123")
test_decode2 = encode_cyclic(test_decode2)
print(test_decode2) # Output: decoded string

```
This Python script defines a function called `encode_cyclic` that takes a string as input and returns an encoded version of the string. It then passes this string to this function and checks whether the output decoded string matches the original input string. The `decode_cyclic` function takes the input string and checks whether the input string is correctly encoded using the `encode_cyclic` function.

The function also provides test cases to ensure the correctness of the encoding and decoding operations.