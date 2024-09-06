```python
def reverse_delete(s, c):
    """
    Removes characters from s that are in c, then checks if the resulting string is a palindrome.
    """
    s = [char for char in s if char not in c]
    return s, s == s[::-1]
```
The method iterates through each character in the input string `s`, using a list comprehension to verify that each character is not included in the unwanted characters listed in `c`, it simply deletes those characters from `s`. After cleaning the string, it checks if it's a palindrome by comparing the cleaned string to its reverse using the slice notation `s[::-1]`. The function returns a tuple containing the processed string and a boolean indicating whether it's a palindrome or not.