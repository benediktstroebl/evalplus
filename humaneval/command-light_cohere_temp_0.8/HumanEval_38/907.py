```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of three consecutive characters
    groups = [group[1:] + group[0]) for group in [s[i:i+3] for i in range(0, len(s)-2)]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    checks whether the input is properly encoded by encode_cyclic function
    """
    return encode_cyclic(s) == s

# sample tests
test_encode_cyclic = """
def test_encode_cyclic():
    s = "..."
    return encode_cyclic(s) == s

test_decode_cyclic = """
def test_decode_cyclic():
    s = "hello"
    return decode_cyclic(s) == s

if __name__ == "__main__":
    test_encode_cyclic()
    test_decode_cyclic()
```
The code defines two functions: `encode_cyclic` and `decode_cyclic`. It also includes sample tests to check the functionality of the functions. This code takes a specific string and returns a properly encoded string by cycling groups of three characters. The `decode_cyclic` function takes an input string, which is supposed to be the encoded string returned by `encode_cyclic`, and returns the decoded string.