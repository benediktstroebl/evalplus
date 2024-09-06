```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same value as s (using s[:0] to create a new string with the same values but different reference)
    for i, char in enumerate(s):
        if char not in delete:
            palindrome += char
    return palindrome, palindrome == palindrome[::-1]
```

The function `reverse_delete()` takes two strings as input and returns a tuple containing the result string after deleting characters in `s` that are present in `c`, along with a boolean indicating whether the resultant string is a palindrome. 

This is achieved by initially creating a new string called `palindrome` with the same value as the input `s`. Subsequently, each character of `s` is iterated through, and if the current character is not contained within the delete list, it is appended to `palindrome`. The resultant string is then returned as the first element of the tuple, while the palindrome check is conducted on the modified string and returned as the second element of the tuple.