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

The function `solve` takes a string as input and iterates through each character in the string. Using the `isalpha()` method, it determines whether each character is a letter. If so, it uses the `swapcase()` method to change the case of the character. If the character is not a letter, it is added to the new string as is. Finally, the function returns the newly constructed string. 

This solves the problem of reversing the string while keeping non-letter characters unchanged, as stated in the markdown code block problem prompt.