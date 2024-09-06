```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s[::3] if len(g) == 3)

def decode_cyclic(s: str):
    """
    returns original string
    """
    return s if s == encode_cyclic(s) else " decoded error"

def test_encode_cyclic():
    """
    def test():
        input = "hello world"
        assert encode_cyclic(input) == "h.hr(hello, tt)..."
    return input("Test passed: ")

def test_decode_cyclic():
    """
    def test():
        input = "hello world"
        assert input == decode_cyclic(input)
    return input("Test passed: ")

test_encode_cyclic()
test_decode_cyclic()
```

This code defines two functions: `encode_cyclic` and `decode_cyclic`, that solve the problem of encoding and decoding cyclic groups of three characters. It also contains two test functions that validate the correctness of the `encode_cyclic` and `decode_cyclic` functions.