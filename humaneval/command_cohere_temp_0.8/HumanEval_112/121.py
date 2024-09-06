```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`, and returns a tuple containing the `delete` string and a boolean value `palindrome`. The purpose of this function is to delete all characters in string `s` that are also present in string `c`, and then determine whether the resulting string is a palindrome. 

The script employs list comprehension to create a list `delete` that contains all characters from string `s` that are not present in string `c`. Then, it reverses the order of the characters in the `delete` list and compares it with the original string `s` to determine whether it's a palindrome. The function finally returns a tuple containing the `delete` string and a boolean value `palindrome`.