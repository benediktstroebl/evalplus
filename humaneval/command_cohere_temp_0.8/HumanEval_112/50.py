```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`, and returns a tuple with the resulting string after deleting characters from `s` that are present in `c`, followed by a boolean indicating whether the resulting string is a palindrome. To achieve this, the script uses lists and list comprehensions to efficiently delete characters from `s` that appear in `c`. The deleted characters are reversed and then reinserted into the string to ensure the correct order. Finally, the script compares the resulting string with its reverse to determine if it's a palindrome. 

The provided code is self-contained and should run correctly with the appropriate inputs.