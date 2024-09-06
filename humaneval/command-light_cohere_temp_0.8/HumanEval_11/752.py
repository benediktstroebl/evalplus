```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings, a and b, consisting only of 1s and 0s.
    - Iterate through length of the shortest substring consisting of all characters from both strings that are either ones (0) or equal to the corresponding character in a. steel you string's characters (ones and zeros) will be the same,
    and thus you can take the shorter one.
    - The maximum length of substring with all ones and zeros is m+n, where m is the length of a and n is the length of b
    - Test string (Longest substring of all ones and zeros):
    - In:
    - a = '010101010101'
    - b = '010101010101'
    - b has the longest substring of ones and zeros
    - Output: 101010101101
    """
    m, n = len(a), len(b)
    s = [0] * (m + n)
    for i in range(m):
        s[i] = a[i]
    for i in range(n):
        s[i + m] = b[i]
    for i in range(m + n - 1):
        if s[i] == 0:
            s[i] = s[i - 1] + 1
    return ''.join(s)
```
This Python function takes two strings a and b, consisting only of ones and zeros, as input. The function performs the maximum length substring with all ones and zeros by iterating over the strings. This substring is the shortest one. The maximum length of substring with all ones and zeros is m+n, where m is the length of a and n is the length of b.