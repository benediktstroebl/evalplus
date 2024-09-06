```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    delete = ''.join(delete)
    return delete, delete == delete[::-1]
```
This Python script defines a function called `reverse_delete` taking two strings as input, `s` and `c`, where `s` is the main string to analyze and `c` is the string of characters to be deleted. This function deletes all characters in `s` that are also present in `c`, and then checks whether the resulting string is a palindrome. The delete variable is initialized with a list of characters in `s` that are not present in `c` and to ensure the resulting string does not have an odd length, the first empty string is appended to `delete`. The characters of `delete` are then reversed and joined into a single string. The function returns a tuple with the resulting string and a boolean indicating whether it is a palindrome.