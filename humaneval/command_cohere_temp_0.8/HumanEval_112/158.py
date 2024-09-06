```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    return (''.join(delete), delete == s)
```

The Python script provided defines a function `reverse_delete` that performs the specified task. It takes two strings, `s` and `c`, as input and returns a tuple consisting of a string and a boolean value.

Here's a step-by-step explanation of how the function works:
1. The function starts by creating a list `delete` using a list comprehension. This list comprehension iterates over each character in the input string `s` and includes only the characters that are not present in the second input string `c`. This step effectively deletes all occurrences of characters that are present in `c` from the string `s`.
2. After deleting the characters, the function then reverses the `delete` list using the `reverse()` method. This step is crucial to ensure that the deleted characters are restored in reverse order, leaving gaps in the string.
3. To handle the case where the string might have leading and trailing gaps after deletion, the function appends an extra empty string `''` to the `delete` list. This ensures that the resulting string will have a consistent length matching the original `s`.
4. Finally, the function returns a tuple with the joined string resulting from the deletion and palindrome check. The palindrome check is performed by comparing the `delete` list with the original `s` string, and the boolean value indicates whether the resulting string is a palindrome.

This code will output a tuple containing the resulting string and a boolean indicating whether the original string was a palindrome after the deletions.