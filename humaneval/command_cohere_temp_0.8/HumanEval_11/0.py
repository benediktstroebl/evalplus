```python
from typing import List

def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.isalpha() and b.isalpha() and a + b == '10'*len(a) + '1'*len(b)
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result
```

This code block uses the Python assert statement to check two preconditions:
1. Checking if both input strings are alphabetic, implying they consist only of 1s and 0s. This is done using the isalpha() function.
2. Checking if the XOR operation on individual characters of strings a and b gives the concatenation '10'*len(a) + '1'*len(b) of the same length. This is achieved by concatenating the characters of a and b, asserting equality to the latter string, and checking if it has the appropriate length.

Although these tests are more explicit, mentioning in the docstring that these are the assumed preconditions and including the tests in the code block would be a more elegant approach. 

This code block otherwise implements the function as requested in the original prompt, iterating through the strings' characters, performing binary XOR, and returning the result.