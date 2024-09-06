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

The function `solve` takes a string as its argument and loops through its characters. In each iteration, it checks if the character is alphabetic using the `isalpha()` method. If true, it uses the `swapcase()` method to change the case of the character. If the character is not alphabetic, it appends it as it is. Finally, the function joins the characters to form the resulting string and returns it. 

This solves the problem as posed in the original prompt.