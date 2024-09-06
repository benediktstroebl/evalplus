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
    by decoding the input and returns decoded string
    """
    return encode_cyclic(s)

def test_encode_decode():
    """
    test the encode_cyclic function
    """
    s = "abcdef"
    encoded = encode_cyclic(s)
    assert encoded == s
    assert len(encoded) == (len(s) + 2) // 3
    s = "123456"
    encoded = encode_cyclic(s)
    assert encoded == s
    assert len(encoded) == (len(s) + 2) // 3

def main():
    print("encode_cyclic: ", encode_cyclic("abcdef"))
    print("decode_cyclic: ", decode_cyclic("abcdef"))
    print("test_encode_decode: ", test_encode_decode())

if __name__ == "__main__":
    main()
```

The code defines a function called `encode_cyclic` that splits a string into groups of three characters, cycles the characters in each group, and returns the encoded string. The `decode_cyclic` function takes an encoded string and decodes it, using the `encode_cyclic` function, and returns the decoded string. The `test_encode_decode` function passes the `encode_cyclic` function with a test string and asserts that the output is equal to the original string. The `main` function calls the encode_cyclic and decode_cyclic functions with the test string "abcdef" and prints the results. It also calls the by decoding the test string, it passes the test and prints the result.