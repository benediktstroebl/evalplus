```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(set(s).intersection(letters)) == 0 else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a string `s` as input. The function inspects each character in the string using a generator expression. If the character is a letter, it toggles its case using the `swapcase()` method. If the character isn't a letter, it remains unchanged. Finally, the function returns the modified string. This behavior is depicted in the given problem statement, where the goal is to invert the case of alphabetic characters while leaving non-alphabetic characters unaffected.

The solution is concise and achieves the problem's intent effectively. It also has a performance advantage over a manual approach using a loop and if statements, especially for large inputs, because Python's string methods are optimized. The `swapcase()` method does the alphabetic character case flipping internally. Additionally, the generator expression leverages Python's list comprehension capabilities, producing a more streamlined and readable solution.