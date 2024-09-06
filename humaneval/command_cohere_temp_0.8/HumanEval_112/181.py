```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` taking two parameters, `s` and `c`, aiming to delete characters in string `s` that are also present in string `c`, and then checking whether the resulting string is a palindrome. The task is performed in two main steps:
1. Creation of a list `delete` that gathers all characters from `s` that are **not** present in `c`. This list is created using a list comprehension, filtering out characters present in `c` from the original string `s`.
2. The list `delete` is then reversed using the `reverse()` method, turning it back to a string. This string is compared to its reverse version (`delete[::-1]`) to check if it's a palindrome. The variable `palindrome` is assigned the Boolean result of this comparison.

The function finally returns a tuple consisting of the `delete` string and the `palindrome` Boolean value. 

This solution adheres to the problem's instructions and delivers the required tuple of the modified string and the palindrome check result.