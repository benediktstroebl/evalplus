```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The problem is to take two strings, `s` and `c`, and delete all the characters in `s` that are present in `c`. We then check whether the modified string is a palindrome. 

This problem can be solved by:
1. Taking a list comprehension to delete the characters present in `c` from `s`.
2. Reverse the remaining string and append the reversed string to the previous list comprehension result.
3. The deleted string will form a palindrome if the original string was a palindrome and the character deletion is done at the center.

The provided solution above showcases these steps in a clear manner. It returns a tuple containing the deleted string and a boolean value (`True` or `False`) depending on whether the modified string is a palindrome. 

This neatly accomplished code is an effective approach to this problem.