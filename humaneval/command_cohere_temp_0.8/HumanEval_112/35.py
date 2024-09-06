```python
def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = [x for x in s if x not in c]
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])
```
The provided Python script defines a function `reverse_delete` which takes two strings, `s` and `c`, as input. It removes characters from string `s` that are present in string `c` using a list comprehension. Then, it compares the modified string `s` with its reverse using slicing (`s[::-1]`) to determine if it's a palindrome. The function returns a tuple containing the modified string `s` and a boolean value indicating whether it's a palindrome. The code efficiently solves the problem and provides the desired output.