```python
def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]

    # Checking if the resultant string is a palindrome
    return (''.join(result), result == result[::-1])
```

This approach uses a list comprehension to filter the string `s` and create a new string (`result`) that contains only the characters not present in string `c`. The function then returns a tuple consisting of the resultant string after deletion and a boolean indicating whether the resultant string is a palindrome or not. This implementation follows the `def` format above and solves the task efficiently.