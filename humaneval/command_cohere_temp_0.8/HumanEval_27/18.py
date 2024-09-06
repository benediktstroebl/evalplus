```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a string that flips the case of every character that is alphabetic, keeping non-alphabetic characters unchanged. This is achieved by using a list comprehension and the `swapcase()` method for each character that is alpha, and keeping the character as is for non-alphabetic characters. 

Would you like assistance with any other problems involving strings and their manipulation? Let's tackle them together!