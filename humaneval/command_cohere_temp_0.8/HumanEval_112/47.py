```python
def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = [x for x in s if x not in c]
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])
```
The provided Python script defines a function `reverse_delete` that takes two strings, `s` and `c`, as input. It uses a list comprehension to remove characters from string `s` that are present in string `c`. Then, it returns a tuple with the modified string `s` and a boolean value indicating whether the resulting string is a palindrome. This is determined by checking if the string is equal to its reverse (`s == s[::-1]`). The function effectively completes the task of removing characters from `s` that are also in `c` and determines if the remaining string is a palindrome.