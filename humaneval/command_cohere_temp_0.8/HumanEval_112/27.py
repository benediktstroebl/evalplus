```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The function `reverse_delete()` takes two strings, `s` and `c` as input and returns a tuple containing the modified string `s` and a boolean indicating if the string is a palindrome. To solve the problem, the following steps were taken:
1. Use a list comprehension to delete characters in `s` that are also present in `c`. This list comprehension effectively removes characters in `s` that appear in `c` and creates a new string, `s`, without those characters.
2. After creating the modified string `s`, the function returns a tuple with the modified string and a boolean. The boolean is `True` if the modified string is the same when reading forward and backward (palindrome), and `False` otherwise. 

This problem can also be solved using `set()`, which can make it a little bit more efficient in terms of time complexity, but the above solution is more straightforward and also efficient. 

This solution will work correctly for the specified test cases.