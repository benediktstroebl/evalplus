### Cyclic Encoding and Decoding

Here's a Pythn script that provides both the `encode_cyclic` and `decode_cyclic` functions:

```markdown
### Code
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    decoded_string = ""
    index = 0
    while index < len(s):
        group = s[index:index + 3]
        if len(group) == 3:
            decoded_string += group[1] + group[0] + group[2]
        else:
            decoded_string += group
        index += 3

    return decoded_string


### Tests
def test_encode_and_decode():
    test_string = "HelloWorld"
    encoded = encode_cyclic(test_string)
    decoded = decode_cyclic(encoded)
    assert decoded == test_string, f"Expected '{test_string}', got '{decoded}'"


if __name__ == "__main__":
    test_encode_and_decode()
    print("Tests passed.")
```

### Usage

You can use the `encode_cyclic` and `decode_cyclic` functions in your Python scripts by importing this module and calling these functions.

For example, you can run the `test_encode_and_decode` function to test the correctness of the encoding and decoding process.