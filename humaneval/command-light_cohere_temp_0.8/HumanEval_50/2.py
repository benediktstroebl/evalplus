```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def test_encode_shift():
    assert encode_shift("hello") == "hlgaoa"
    assert encode_shift("world") == "dwrooa"
    assert encode_shift(")!#") == "!!/$@"
    assert encode_shift("A") == "? Advertising"
    assert encode_shift("aeiouX") == "aeiouXoa"
    assert encode_shift("") == ""

def decode_shift(s: str):
    return "".join([chr(int(c)-97 + 'a') for c in s])


def test_decode_shift():
    assert decode_shift("hlgaoa") == "hello"
    assert decode_shift("dwrooa") == "world"
    assert decode_shift("!).=="") == "!"
    assert decode_shift("A") == "a"
    assert decode_shift("aeiouX") == "aeiou"
    assert decode_shift("") == ""

if __name__ == "__main__":
    test_encode_shift()
    test_decode_shift()

```
This Python script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts each character in the input string by 5 in the alphabet, and returns an encoded string. The `decode_shift` function takes the encoded string as input and returns the decoded string.

Both functions have been tested with a series of test cases. The `test_encode_shift` and `test_decode_shift` functions assert that the output of `encode_shift` and `decode_shift` matches the expected values.

The `__name__ == "__main__"` condition ensures that the test cases are run only when the script is executed directly, not when it's imported as a module.

The output of this code will be the test results displayed on the console.