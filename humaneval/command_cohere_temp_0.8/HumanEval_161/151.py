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

The function `solve` takes a string as an input and loops through its characters. In each iteration, it checks if the character is alphanumeric using the method `isalpha()`. If it is, the method `swapcase()` is used to swap the case of the character. If the character is not alphanumeric, it is added to the new string as is. The final string is returned after all characters have been processed. 

This solves the problem as stated in the prompt, where any non-letter characters are left as they are, while letters have their case reversed.