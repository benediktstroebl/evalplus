```python
def reverse_delete(s, c):
    """Removes characters from s that are in c, then checks if the result is a palindrome."""
    s = [char for char in s if char not in c]
    return s, s == s[::-1]
```

This Python script defines a function called `reverse_delete` that takes two strings as input, `s` and `c`. This function removes all characters from string `s` that are present in string `c` and then checks whether the resulting string is a palindrome. A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward. The function returns a tuple, the first element of which is the modified string `s`, and the second element of which is a boolean that indicates whether the string is a palindrome. This is accomplished by using a list comprehension to create a new string `s` from the characters of the original string `s` that are not in string `c`. The result is returned as a tuple of the new string and whether it's a palindrome when read forwards and backwards. This is determined by using the slice notation `s[::-1]` to reverse the new string and then comparing it to the original modified string.