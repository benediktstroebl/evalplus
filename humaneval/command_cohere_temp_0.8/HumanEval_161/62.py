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

This code defines a function `solve` taking one parameter `s`, which performs the character transformations according to the problem statement. 

The `solve` function iterates through each character in the input string `s`. For each character, it checks if it is an alphabetic character using the `isalpha()` method. If it is, it uses the `swapcase()` method to change the case of the character. This method swaps the case of the character between lowercase and uppercase. If the character is not alphabetic, it is appended to the `new_str` list as it is. Finally, the function returns the joined string from the `new_str` list.

This code addresses the problem requirements mentioned in the original request, and should produce the desired output for the given examples. 
To test this code, run it in your local Python environment and verify that the behavior aligns with the problem statement and the expected outputs. 
You can also use this code as a starting point and adapt it to suit other similar challenges that involve character-level transformations in strings.