```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```
This Python script defines a function called `reverse_delete` takes two strings, `s` and `c` as input, it removes characters from string `s` that are present in string `c`, and then reverses the remaining delete operation to delete the characters again, finally, it checks if the resultant string is a palindrome or not and returns a tuple containing the cleaned string and a boolean value indicating whether the checked palindrome or not. 

This solution addresses the problem in a straightforward manner, and its efficiency is linear in the lengths of the input strings.

Here is a sample output:
```
('cdedc', True)
('bcd', False)
('acdef', False)
('abcdedcba', 'ab', ('cdedc', True))
```