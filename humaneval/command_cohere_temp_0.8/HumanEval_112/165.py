```python
def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = [c for c in s if c not in c]
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])
```
The `reverse_delete` function takes two strings, `s` and `c`, as input. It uses a list comprehension to remove all characters from `s` that are present in `c`. Then, it compares the resulting string with its reverse using slicing (`s[::-1]`) to determine whether it's a palindrome. The function returns a tuple containing the modified string `s` and a boolean value indicating whether the string is a palindrome.