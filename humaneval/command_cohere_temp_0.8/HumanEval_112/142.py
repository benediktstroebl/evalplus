```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` taking two strings as input, `s` and `c`, aims to delete characters in string `s` that are also present in string `c`, then checks if the resulting string is a palindrome. The task is performed in the `delete` list, which is then reversed to match the order of the original string `s`. The variable `palindrome` is assigned the value `True` if the `delete` list matches the original string `s` and `False` otherwise. The function returns a tuple containing the `delete` list and the `palindrome` boolean value.