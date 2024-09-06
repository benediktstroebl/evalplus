```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two arguments, `s` and `c`. The function uses two arrays to delete all the characters in `s` that are equal to any character in `c`, and these two steps are done in a backward fashion to preserve palindrome checking correctness. The function then checks whether the resulting string is a palindrome. The function returns a tuple containing the result string and a boolean value (`True` or `False`) indicating whether the check was successful. 

Here is a breakdown of the code:
1. `delete = [x for x in s if x not in c]`: This line creates a new list called `delete` and initially fills it with all the characters in `s` that are not in `c`. This list will contain all the characters to be deleted from the original string.
2. `delete.reverse()`: This line reverses the order of characters in the `delete` list. This is done to maintain the correctness of the palindrome check. Since the original string is not modified, we need the deletion list to be in reverse order.
3. `palindrome = True if delete == s else False`: This line checks whether the reversed deletion list (`delete`) is equal to the original string (`s`). If all the characters in `s` that were present in `c` were removed, then `delete` would be equal to `s`, and the function returns `True`. Otherwise, it returns `False`. 

The function returns a tuple containing the `delete` list and the `palindrome` boolean value.