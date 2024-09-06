```python
def reverse_delete(s, c):
    """
    Removes characters from s that are in c, and checks if the resulting string is a palindrome.
    """
    s = [char for char in s if char not in c]
    reversed = s[::-1]
    equal = all(x == y for x, y in zip(s, reversed))
    return (''.join(s), equal)
```
The solution utilizes list comprehension and slicing to filter out characters in `s` that appear in `c`, resulting in a new string. The variable `reversed` is created by slicing the reversed string from `s` to compare characters easily. The `all()` function is then used to check if the resulting string after reversal is equal to the original string, indicating if it's a palindrome. The function returns a tuple consisting of the modified string and a boolean value indicating whether it's a palindrome.