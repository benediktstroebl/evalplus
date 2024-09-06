```python
def solve(s):
    new_str = []
    for c in s:
        if c.isalpha():
            new_str.append(c.swapcase())
        else:
            new_str.append(c)
    return ''.join(new_str)
```

This Python script defines a function `solve` that takes a string `s` as input and performs the tasks specified in the problem statement. It examines each character in the input string using the `isalpha()` method. If the character is alphabetical, it uses `swapcase()` to change its case, whether it is uppercase or lowercase. Otherwise, if the character is not a letter, it remains unchanged. The characters are accumulated in the `new_str` list, and then joined into a single string for the final output.