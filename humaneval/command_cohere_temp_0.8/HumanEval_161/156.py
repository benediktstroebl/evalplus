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

This code defines a function `solve` taking one parameter `s`, which performs the character transformations outlined in the problem statement. It iterates through each character in the input string `s`. For alphabetic characters, it uses the `swapcase()` method to reverse their case, whereas, for non-alphabetic characters, it retains their original form. The resulting characters are concatenated into a new string and returned.

The `solve` function's appropriateness is demonstrated by the supplied example scenarios, which yield the predicted results.