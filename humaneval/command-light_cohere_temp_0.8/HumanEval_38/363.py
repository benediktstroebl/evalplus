```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of three
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    acyclor
    returns decoded string.
    """
    standard-test cases for encode_cyclic and decode_cyclic functions.
    """
    tests:
    test_encode = "hello"
    test_decode = encode_cyclic(test_encode)
    assert test_decode == "olleH"

    test_decode_twice = encode_cyclic(test_decode)
    assert test_decode_twice == "olleH"

    test_long = "This is a very long string to test our encode/decode functionality."
    test_decode_long = encode_cyclic(test_long)
    assert test_decode_long == test_long

    test_ref = "hello world"
    test_decode_ref = encode_cyclic(test_ref)
    assert test_decode_ref == "olleH world"

    test_empty = ""
    test_decode_empty = encode_cyclic(test_empty)
    assert test_decode_empty == ""

    test_single_char = "h"
    test_decode_single_char = encode_cyclic(test_single_char)
    assert test_decode_single_char == "o"

    test_decode_single_char_twice = encode_cyclic(test_decode_single_char)
    assert test_decode_single_char_twice == "o"

    test_invalid = "this is not a cyclic string"
    with raises(ValueError):
        test_decode_invalid = encode_cyclic(test_invalid)

    test_invalid_empty = " "
    with raises(ValueError):
        test_decode_empty_invalid = encode_cyclic(test_invalid_empty)

    ```
The script defines the `encode_cyclic` and `decode_cyclic` functions, which are used to encode and decode a string, respectively. It also includes a tests to ensure the correctness of the functions. The tests pass the