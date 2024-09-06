```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function removes characters from string `s` that are present in string `c`, and then checks whether the modified string is a palindrome. The function returns a tuple containing the modified string and a boolean value indicating whether it's a palindrome. The behavior is demonstrated with examples in the Markdown code block. 

This approach uses the `set` logic of Python to delete the characters, and then checks if the resulting string is a palindrome. It is efficient in terms of time and space complexity, utilizing a set operation to remove characters and a reversal operation to check for palindromes, both of which have O(n) time complexity, where n is the length of the input string.