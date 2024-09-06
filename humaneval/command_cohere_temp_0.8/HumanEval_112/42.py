```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function deletes characters in string `s` that are also present in string `c`, and then checks whether the remaining string is a palindrome. The function returns a tuple containing the edited string `delete` and a boolean value `palindrome` that indicates whether the string is a palindrome. The deletion process is handled by creating a list of characters in `s` that are not in `c`, which is then reversed to achieve the desired deletion effect. The palindrome check is performed by comparing the reversed list to its original iteration order, and saving the result in `palindrome`. Overall, the provided code solves the problem statement in a concise and effective manner.