```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    first we not match
    encoded string.
    return s.decode_cycl(encode_cyclic(s))


# test cases
def test_encode_decode():
    assert encode_cyclic("abcad") == "...abc".
    assert encode_cyclic("...adf") == "...adf"
    assert encode_cyclic("....") == "....."
    assert encode_cyclic("") == ""
    assert encode_cyclic("hello") == "..."hello"

def main():
    print(test_encode_decode())

if __name__ == "__main__":
    main()
 ```

The code implements a function encode_cyclic that converts a given string into its cyclic encoding and a function decode_cyclic that converts the cyclic encoding back into the original string. The main function executes these tests that verify the correctness of the encode_cyclic and decode_cyclic functions.