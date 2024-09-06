```python
def reverse_delete(s, c):
    """
    Deletes characters in s that are present in c, then checks if the result is a palindrome.
    """
    s = [x for x in s if x not in c]
    palindrome = s == s[::-1]
    return ("".join(s), palindrome)
```
The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string `s` with characters deleted from `c` and a boolean indicating whether the modified string is a palindrome.

To solve the problem, the following steps were followed:
1. Remove all characters from s that are present in c: To remove the characters present in the string c from the string s, the list comprehension `[x for x in s if x not in c]` is used. All characters in s that are not in c are retained, and the resulting string is formed.
2. Check if the resulting string is a palindrome: After removing the characters from s, the modified string is checked for whether it is a palindrome. This is done by comparing the original string with its reverse (`s == s[::-1]`).

The script, when provided with the input tests, returns the correct values.

For example:
```python
>>> reverse_delete("abcdef", "b")
('acdef', False)
>>> reverse_delete("abcde", "ae")
('bcd', False)
>>> reverse_delete("abcdedcba", "ab")
('cdedc', True)
``` 
The script passes all the tests and satisfies the problem requirements, therefore.