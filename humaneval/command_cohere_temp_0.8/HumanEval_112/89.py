```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`. This function deletes characters from string `s` that are present in string `c`, and then checks whether the modified string is a palindrome. It returns a tuple containing the modified string and a boolean value indicating whether it's a palindrome. The delete string is initialized by using a list comprehension that filters out the characters in s that are not in c. Then, the list comprehension reverses the delete string and appends the characters in s that are in c. This ensures that characters in s that are in c are appended after the reverse deletion. The final delete string is returned as the first element of the tuple, and the boolean result of whether it's a palindrome is returned as the second element.