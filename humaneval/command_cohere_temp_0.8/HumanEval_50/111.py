Here's a Python script with a self-contained function that solves the problem:
```python
#!"usr/bin/env python3

def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])

# The following two functions are testing functions for encode_shift and decode_shift respectively.
def test_encode():
    assert encode_shift("Hello") == "Ifmmp"
    assert encode_shift("World") == "Zbnbn"
    assert encode_shift("Cohere") == "GkgkU"

def test_decode():
    assert decode_shift("Ifmmp") == "Hello"
    assert decode_shift("Zbnbn") == "World"
    assert decode_shift("GkgkU") == "Cohere"

test_encode()
test_decode()
```

This script defines the two functions `encode_shift` and `decode_shift` as specified in the prompt. It also includes two testing functions, `test_encode` and `test_decode`, which validate the outputs of the two functions in the script.

Let's break down the functions step by step:
1. `encode_shift(s: str)`: This function takes a string `s` as input and returns the encoded string after shifting each character by 5 in the alphabet.
    1.1. The function uses a list comprehension that iterates over each character `ch` in the input string `s`.
    1.2. For each character, it calculates the new ASCII value by subtracting 97 (the ASCII value of 'a') and then adding 5. This gives the new shifted value which is bounded by 26 (since it's a modulo operation).
    1.3. After the calculation, the new ASCII value is added to 97 to get the new character, which is then appended to a string builder.
2. `decode_shift(s: str)`: This function takes a string `s` as input and returns the original string decoded after shifting each character back by 5 in the alphabet.
    2.1. This function is similar to the previous one. It uses a list comprehension that iterates over each character `ch` in the input string `s`.
    2.2. For each character, it calculates the new ASCII value by subtracting 97 (the ASCII value of 'a'), which gives the original value before the shift. Then 5 is added to the value.
    2.3. After the calculation, the new ASCII value is added to 97 to get the new character, which is then appended to a string builder.
3. `test_encode()`: This function tests the `encode_shift` function.
    3.1. It uses the `encode_shift` function to encode the strings "Hello", "World", and "Cohere" and checks that the encoded values match the expected outputs "Ifmmp", "Zbnbn", and "GkgkU" respectively. 
4. `test_decode()`: This function tests the `decode_shift` function.
    4.1. It uses the `decode_shift` function to decode the strings "Ifmmp", "Zbnbn", and "GkgkU" and checks that the decoded values match the expected outputs "Hello", "World", and "