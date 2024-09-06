Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    XOR two strings consisting only of ones.
    a: Convert the input to lists of characters
    b: Convert input to lowercase
    c: Remove all characters not in set of uppercase letters
    d: Concatenate all elements in lists a and b
    e: Convert concatenated string back to a string
    """
    a = [c for c in a if c.isalpha()]
    string_like(a)
    b = [c for c in b if c.isalpha()]
    string_like(b)
    result = ''.join(c for c in string.join([a, b]) if c.isalpha())
    main()
result = string_xor('010', '110')
print(result)
```
The function takes two strings as input, consisting only of ones, and returns the XOR of these two strings. The code then runs the string manipulation functions like `string_like`, `islower`, `join`, `remove`, and `concat`. The function also contains comments that describe the purpose of each line of code.