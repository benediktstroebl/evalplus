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

The function `solve` takes a string as input and iterates through each character in the string. If the character is alphanumeric, it uses `swapcase` which swaps the case of the character from lower to upper, or vice versa. If the character is not alphanumeric, it is appended to the new string as is. The final string is returned after all characters have been processed. This solves the problem of reversing the string while keeping non-letter characters intact.