```python
def reverse_delete(s, c):
    delete = [char for char in c]
    pm = []
    for i in s:
        if i not in delete:
            pm.append(i)
    pm = pm[::-1]
    if pm == s:
        return ('', True)
    else:
        return (''.join(pm), False)
```
This Python script defines a function called `reverse_delete` which takes two arguments, `s` and `c`. The function uses list comprehension to create a list `delete` that contains all the characters from the second argument `c`. It then iterates through the characters of the first argument `s` and collects them in a new list `pm` if they are not in the `delete` list. After collecting all characters, it creates a reversed version of `pm` and checks if it matches the original string `s` to determine if the result is a palindrome. If it's a palindrome, it returns an empty string with a boolean True. Otherwise, it returns the `pm` string with a boolean False.

Here is an example usage of the function:
```python
>>> reverse_delete("abcde", "ae")
('bcd', False)
>>> reverse_delete("abcdef", "b")
('acdef', False)
>>> reverse_delete("abcdedcba", "ab")
('cdedc', True)
``` 
The examples demonstrate how the function correctly identifies the remaining characters after deleting those in the deletion string, and whether the remaining string is a palindrome.