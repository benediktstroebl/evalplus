Here is a self-contained Python script with a function that solves the problem of XORing two strings in markdown code blocks:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """ XOR two strings consisting only of 1s and 0s into a single string.
    A -> Input
    string consisting of 0s and 1s only
    B> Input the other string
    """
    # Remove all non-numeric characters
    a = ''.join(char for char in a if char.isdigit())
    it
    remove_non_numeric(b), a)
    return a + b

def remove_non_numeric(string: str, result: List[str]) -> str:
    for char in string:
        if char.isdigit():
            result.append(char)
    if char != ' ' and char != '\n':
            result.append(char)
    return ''.join(result)

test_string_xor = """
    1010
    101
    10010
    111
    0
    11
    10
"""
test_strings = [test_string_xor] * [r"12\n"] * [r"13\n"\])

for test_string in test_strings:
    print(test_string, end='')
    print('', end='')
    print(string_xor(test_string, test_string[::-1]))
    print('', end='')
```

This script defines a function `string_xor` that performs a XOR operation on two input strings, each composed of only digits and spaces. It also includes a helper functions `remove_non_numeric` to remove non-numeric characters from the input strings and test cases.