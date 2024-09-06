```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) else s[::-1]
```
The function leverages the `swapcase()` method to flip the case of letters in the string, while disregarding non-letter characters. Non-letter characters are considered unchanged. In the event the string contains no letters, the function reverses the entire string using the slicing technique `s[::-1]`. This approach is tested and confirmed to pass all the given test cases.