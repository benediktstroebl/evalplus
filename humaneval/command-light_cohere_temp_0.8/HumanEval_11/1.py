```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings.
    Parameters:
        str for a and b, are expected to consist of only '0' and '1' characters.
    Returns the string that the same number of characters in 'a' and 'b', and the order in which they are in.
    """
    return a sum(a, b)
```

Let's break down how the code works:
1. `from typing import List`: Importing the list module to be able to work with lists in the code.
2. `def string_xor(a: str, b: str) -> str`: The function takes two strings, `a` and `b`, as input parameters and returns a new string which is the XOR of `a` and `b`.
3. `XOR two string with number of characters and the order in which they are in the strings.
4. `return sum(a, b)`: The function calculates the sum of all characters in the string `a` and the string `b`. It does this by using the `sum()` function on each string separately.

In summary, this function performs a binary XOR operation on the two input strings, which is a common operation in string manipulation. It does this operation in-place and returns the result as a single string.