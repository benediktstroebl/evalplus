```python
def reverse_delete(s, c):
    # Filter and delete characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the remaining string is a palindrome
    return s, s == s[::-1]
```
The provided Python script defines a function `reverse_delete` taking two strings `s` and `c` as input, aimed at identifying and eliminating characters present in `s` that also appear in `c`. The function constructs a new string by iterating through each character in `s`, omitting any character that corresponds to an element in `c`. Subsequently, it returns a tuple consisting of the modified string and a boolean value. This boolean value is `True` if the remaining string is a palindrome (i.e., reads the same forwards and backward), and `False` otherwise. The example usages showcased in the task statement yield correct results upon execution, accurately reflecting the expected behavior.