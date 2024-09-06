```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` taking two strings as input, `s` and `c`, designed to eliminate characters in string `s` that are also present in string `c`, essentially creating a new string, `delete`, and then checking whether the modified string is a palindrome. The task is achieved through the following steps:
1. Use a list comprehension to create a new list, `delete`, containing all characters in `s` that are NOT present in `c`.
2. Reverse the `delete` list using the `reverse` method. This is done to maintain the original order of characters in `s` before deletion.
3. Compare the modified list, `delete`, with its reverse, `delete[::-1]`, to determine if it's a palindrome. If the two lists are identical, the original string was a palindrome after removing the specified characters.

The function returns a tuple consisting of the `delete` list and a boolean value (`True` or `False`) indicating whether the modified string is a palindrome. 

The provided example usage demonstrates the function's capabilities and highlights its ability to handle different scenarios and input types. When you need to remove specific characters from a string and subsequently assess whether it remains a palindrome, the `reverse_delete` function can be invaluable. 

This approach provides a clear and concise solution to the problem, easily adaptable to different scenarios and with the flexibility to deal with various input types.