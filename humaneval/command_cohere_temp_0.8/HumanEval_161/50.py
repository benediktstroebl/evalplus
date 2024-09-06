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

This Python script defines a function called `solve` that takes a string as input. It goes through each character in the string using a loop and checks if it is an alphabetic character using the `isalpha()` method. If it is, the character's case is swapped using the `swapcase()` method. If the character is not alphabetic, it's added to the `new_str` list as is. Finally, the function returns the joined string from the `new_str` list. This ensures that for non-alphabetic characters, the string remains unchanged, while alphabetic characters have their case reversed.