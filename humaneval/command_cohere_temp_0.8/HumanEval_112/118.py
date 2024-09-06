```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```
The provided Python script solves the problem by removing characters from string `s` that are present in string `c`, resulting in a new string. Then, it checks if this new string is a palindrome by comparing it to its reverse using slicing notation `s[::-1]`. The function returns a tuple containing the created string and a boolean value indicating whether it's a palindrome. 

This approach ensures that all mentioned test cases lead to expected behavior.