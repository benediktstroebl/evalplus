```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the problem statement description, it iterates through each character `c` in the input string `s`. For each character, it checks if it is alphanumeric using the `isalpha()` method. If true, it swaps its case using the `swapcase()` method, which changes the character case to the opposite, and this result is joined to a string that is returned. Otherwise, if the character is not alphabetic, it is appended to the string as is. Thus, the function reverses the string for the case of no alphabetic characters, and reverses the case of each alphabet character elsewhere.