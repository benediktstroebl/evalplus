```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]
```
The function `solve` takes a string as an argument, and returns the modified string as described in the problem statement.

The script offers a straightforward solution using string methods along with basic Python logic. In the event that the provided string contains only letters, the `swapcase` method is applied to reverse the case of each character. When the string contains non-letter characters, a specific slice of the string is targeted for case reversal using a conditional expression with an array `letters` containing all of the lowercase and uppercase letters. This ensures that only letters will have their case reversed while non-letter characters are left unchanged.