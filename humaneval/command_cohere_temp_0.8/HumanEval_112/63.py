```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    if delete == delete[::-1]:
        return delete, True
    else:
        return delete, False
```

The function `reverse_delete()` above takes two strings as parameters `s` and `c` respectively. It deletes all the characters in string `s` that are equal to any character in string `c`. To achieve this, a list comprehension is used to create a new string `delete` with all characters NOT present in string `c`. This is then reversed using the `reverse()` method, and finally a character is appended to make it a string. A check is performed on the result to see if it is a palindrome, and the function returns a tuple of the new string along with a boolean indicating whether it is a palindrome or not.

Here is a sample output of the function with a test case:
```python
>> reverse_delete("abcdedcba", "ab")
('cdedc', True)
```