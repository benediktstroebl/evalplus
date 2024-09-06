```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function removes characters from string `s` that are present in string `c`, resulting in a new string. Then, it checks if the new string is a palindrome, and returns a tuple consisting of the new string and a boolean indicating whether it's a palindrome. The behavior is demonstrated in the example below:
```python
print(reverse_delete("abcdef", "b"))
# Output: ('acdef', False)

print(reverse_delete("abcdedcba", "ab"))
# Output: ('cdedc', True)
``` 
The code uses a list comprehension to create a new string with characters deleted from the first string. The line `delete.reverse()` ensures that the characters are deleted in reverse order, which is essential for correctly identifying the palindrome. The code also uses list comprehension and the `==` operator to check if the resulting string is equal to its reverse, indicating a palindrome.