```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`, and performs a series of operations to solve the specified problem. 

The function first creates a list called `delete` using a list comprehension, which filters out any characters from string `s` that are present in string `c`. This essentially removes the characters from `s` that are equal to those in `c`. The operation `delete.reverse()` flips the order of the characters in the `delete` list, ensuring it becomes the reversed version of the original string `s`. 

The line `palindrome = True if delete == s else False` compares the modified string `delete` with the original string `s`. If the two strings are equal, the function sets the `palindrome` variable to `True`, indicating that the modified string is a palindrome. If the strings are not equal, `palindrome` is set to `False`. 

Finally, the function returns a tuple containing the `delete` string and the `palindrome` boolean value, providing a solution to the problem which indicates whether the modified string is a palindrome and includes only the characters unique to the original string `s`. 

This script enables efficient problem-solving for the given task, where it is required to remove characters from a string that are also present in another string and then determine if the modified string is a palindrome. The use of list comprehension and string manipulation techniques makes it concise and effective.