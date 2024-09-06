Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and how to use it:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return encode_shift(s, shift=(-5))
```

The functions can be used as follows:
```python
# Before running the script, make sure to install the required package 'pytest'
import pytest

# Define strings for testing
test_string_1 = "World"
test_string_2 = "Hello, Greetings!"

# Test the encode_shift function
def test_encode_shift():
    encoded_string = encode_shift(test_string_1)
    decoded_string = decode_shift(encoded_string)

    assert test_string_1 == decoded_string
    assert encoded_string != test_string_1

# Test the decode_shift function
def test_decode_shift():
    decoded_string = decode_shift(test_string_2)
    encoded_string = encode_shift(test_string_2)

    assert test_string_2 == decoded_string
    assert encoded_string != test_string_2
```

This script includes two test functions, 'test_encode_shift' and 'test_decode_shift', which verify the correctness of the 'encode_shift' and 'decode_shift' functions, respectively. These tests use the 'pytest' framework, which is a popular testing library in Python. The test_string_1 and test_string_2 are arbitrary strings used to feed the functions and compare the output with the expected decoded strings.

You can run these tests to verify that the functions behave as expected using the command `pytest` in the script's directory.  Any compatible Python version should be able to run this script. You can execute it directly in an IDE or command line interface after modifying the script.