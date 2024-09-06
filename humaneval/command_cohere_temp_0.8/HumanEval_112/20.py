```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function deletes characters in `s` that are also present in `c`, and then checks whether the remaining characters form a palindrome. The function returns a tuple containing the modified string `delete`, and a boolean value `palindrome` that indicates whether the remaining string is a palindrome. 

This code snippet can be tested against different inputs to verify its functionality against the problem statement.