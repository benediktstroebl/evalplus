Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", " Incentiviheywujkiolmnvqz"))
```
The `encode_shift` function shifts every character by 5 in the alphabet, while the `decode_shift` function reverses this operation to decode the string. You can test these functions by calling them with an input string and comparing the output to the original input. 
This approach uses the `translate` method to create a translation table and then translate the input string using this table, which provides a more efficient solution. GIVEN:
```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
```

EXPECTED:
```python
import string

def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    translate_table = str.maketrans("abcdefghijklmnopqrstuvwxyz", " Incentiviheywujkiolmnvqz")
    return s.translate(translate_table)
```