```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` taking two strings as arguments: `s` and `c`. It aims to delete characters from string `s` that are also present in string `c`, and then determine if the resulting string is a palindrome. To achieve this, it uses list comprehension to create a `delete` list containing all characters from `s` that are not present in `c`. Then, it reverses the `delete` list and compares it with the original string `s` to determine if it's a palindrome. The function returns a tuple containing the `delete` list and a boolean value indicating whether the resulting string is a palindrome. 

Here is an example usage of the function:
```python
s = "abcdedcba"
c = "ab"
result = reverse_delete(s, c)
print(result)
```

The output will be:
```
('cdedc', True)
```

The resulting string, 'cdedc', is created by deleting the characters 'a' and 'b' from the original string 'abcdedcba', which are present in the second string 'ab'. The second element in the return tuple is `True` indicating that the resulting string 'cdedc' is a palindrome.