```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz'].swapcase()
```
The code utilizes Python's str.swapcase() function to handle the string's case. If the string contains no letters, it reverses the entire string using str.swapcase(). If the string contains letters, it applies str.swapcase() only to the letters (using the condition letters == 'abcdefghijklmnopqrstuvwxyz' to locate them), and then reverses this result using another str.swapcase(). This addresses the problem's request to reverse letter cases while keeping non-letter characters unchanged.