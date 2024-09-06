```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function deletes characters in `s` that are also present in `c`, and then checks whether the remaining characters form a palindrome. The function constructs a list `delete` by filtering out characters from `s` that are not present in `c`. To ensure the characters are deleted in reverse order, the list is reversed using the `reverse` method, resulting in the modified string. The function then checks if the modified string is a palindrome by comparing it to its reverse using slicing notation `[::-1]`. If the modified string is equal to its reverse, the variable `palindrome` is assigned `True`; otherwise, it is assigned `False`. The function returns a tuple containing the modified string and the `palindrome` boolean value.