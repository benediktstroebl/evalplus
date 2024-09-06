```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the result string after deleting characters in `s` that are present in `c`, along with a boolean indicating whether the resulting string is a palindrome.

To solve the problem, the script uses two strings: `delete` and `reverse`. The `delete` string contains all characters in `c` in the same order. The `reverse` string is the reverse of the original string `s`. The script joins the characters of `s` that are not in the `delete` string and are present in the `reverse` string (thus excluding characters that would disrupt the palindrome). The result is then returned as a tuple with the modified string and a boolean indicating whether the modified string is a palindrome.