```python
def reverse_delete(s, c):
    s_set = set(s)
    c_set = set(c)
    # delete characters in s that are in c
    s = ''.join(x for x in s if x not in c_set)
    # check if the result is a palindrome
    return (s, s == s[::-1])
```
The provided Python script defines a function `reverse_delete` that takes two strings, `s` and `c`, as input. It removes characters from string `s` that are present in string `c`, resulting in a modified string. Then, it checks whether the modified string is a palindrome by comparing it with its reverse using slicing (`s[::-1]`). The function returns a tuple containing the modified string and a boolean value indicating whether it is a palindrome. 

This code can be tested against examples to ensure it meets the problem requirements.