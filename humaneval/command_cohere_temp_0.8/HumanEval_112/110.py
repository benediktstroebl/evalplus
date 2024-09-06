```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return ("".join(delete), palindrome)
```

The problem is solved by using two nested lists: one to hold the characters to be deleted and one to determine if the string is a palindrome. The outer list, `delete`, is populated with all the characters in `s` that are not in `c`. This is done using the list comprehension: `delete = [x for x in s if x not in c]`. The inner list, called `palindrome`, is created by comparing the characters in `delete` to their reversed versions. This is achieved by reversing `delete` and then comparing it to the original, using the slicing notation `delete[::-1]`. Finally, the inner list is checked for equality with the outer list, which determines whether the string is a palindrome. The final result is returned as a tuple containing the joined string of delete and the value of palindrome.