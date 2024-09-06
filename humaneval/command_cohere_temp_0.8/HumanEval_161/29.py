```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the given string's characters, it either swaps the case of letters or keeps non-letter characters as is, and ultimately returns the modified string. This behavior is defined by the `join` function, which concatenates the modified characters together. 

This solves the problem as explained in the prompt, where for letter characters, the case is swapped between upper and lower, while for non-letter characters, the character is kept the same. 

The self-contained nature of the Python script means that it is independent and does not rely on external modules or dependencies. 

This code snippet can be easily copied and executed, and it will correctly solve the problem as stated in the prompt.