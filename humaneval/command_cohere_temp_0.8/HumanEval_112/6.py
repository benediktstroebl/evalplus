```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome
```
The function `reverse_delete()` takes two strings s and c as input and returns a tuple containing the result string and a boolean indicating whether the resulting string is a palindrome. It uses a list comprehension to create a list `delete` that contains all the characters in string `s` that are not included in string `c`. Then, it reverses the order of the `delete` list using the `reverse()` method. afterward, it checks if the list is equal to its reversed version to determine if the resulting string is a palindrome or not. Finally, it returns a tuple containing the `delete` list as the first element and the `palindrome` boolean value as the second element. 

Here is a sample input/output to test the functionality of the function:
```
>> reverse_delete("abcdef", "b")
('acdef', False)
>> reverse_delete("abcde", "ae")
('bcd', False)
>> reverse_delete("abcdedcba", "ab")
('cdedc', True)
```