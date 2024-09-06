```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    b = b.strip(".")
    b = b.strip("!")
    b = b.strip("?")
    rotations = [b[i:]+b[:i] for i in range(len(b)/2)]
    return any(rot in a for rot in rotations)
```
The function rotates the second word through all possible iterations and compares each iteration to the first word. Finally, the function returns `True` if any of the rotations match and `False` otherwise. 

Here is a more concise solution using Python's `re` module for pattern matching:
```python
import re

def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    return bool(re.search(b, a)) or any(re.search(rot, a) for rot in re.split(b, a))
```

This uses a regular expression to find if the second parameter is a substring in the first by using the `re.search` function. We also use the fact that `re.split` creates all possible rotations of the second word.