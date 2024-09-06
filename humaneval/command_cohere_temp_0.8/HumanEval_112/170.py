```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The function `reverse_delete()` takes two strings, `s` and `c` as input and returns a tuple containing the string `s` after deleting characters that appear in string `c` and a boolean indicating if the resulting string is a palindrome. 

The script passes the test and returns the correct values for the examples you provided. Let’s break down how it works:
1. The first line uses a list comprehension to create a new list `s` with all the characters removed from `s` that are in `c`. This is done by iterating over the characters in `s` and checking if each character is not in `c`, if so, the character is added to the new list.
2. The second line then joins the resultant list into a string, giving us the string `s` with all the characters deleted that are in `c`.
3. The final line of the function returns a tuple of the resultant string and a boolean indicating if the string is a palindrome by checking if the resultant string is equal to its reverse. 

This function is self-contained, meaning that it does not rely on any external variables or functions. All the necessary operations are performed within the function, making it easy to reuse and test separately.