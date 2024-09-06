Here's a Python script with a self-contained function that solves the problem:
```python
#!, encode_shift, and decode_shift functions
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
#shift_encoding_decoding.py
#This script implements two functions, encode_shift and decode_shift.

#The encode_shift function takes a string s as input and returns the encoded string.

#The decode_shift function takes a string s as input and returns the decoded string.

#Both functions are implemented using a list comprehension.

#The tests dictionary maps input strings to expected output strings.

#The test_encode_shift and test_decode_shift functions both use the assertInEquals function from unittest.mock.

#This function is used to test that the encode_shift function returns the expected output for a given input.

#The function takes three arguments:
#- expected: The expected output of the encode_shift function
#- actual: The output of the encode_shift function
#- message: A message to display if the assert fails

#The function uses the assertInEquals function to check that the expected string is
#contained within the actual string.

#The function returns None.

tests = {
    "hello": "ifomratlde",
    "world": "jpclemfivce"
}

for key in tests:
    print(f"Testing encode_shift({key})...")
    test_encode_shift(tests[key], encode_shift(key), f"encode_shift({key}) failure.")

for key in tests:
    print(f"Testing decode_shift({tests[key]})...")
    test_decode_shift(tests[key], decode_shift(tests[key]), f"decode_shift({tests[key]}) failure.")

def test_encode_shift(expected, actual, message):
    assertInEquals(expected, actual, message)

def test_decode_shift(expected, actual, message):
    assertInEquals(expected, actual, message)
```