```python
def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the remaining string is a palindrome
    return ''.join(result), result == result[::-1]
```

This approach uses list comprehension to filter the characters of the string `s` that are not in the string `c`, resulting in the `result` string. Then, the characters are joined back to form the resultant string that is checked for being a palindrome, and the result is returned as a tuple of (`result`, `is_palindrome`). 

Here, the `is_palindrome` is a boolean value determined by checking if the `result` is the same when reading backwards (`result[::-1]`) as it is when reading forwards. 

The basic logic for the problem is to remove characters in string `s` that are also present in string `c`, and then determine whether the resultant string is a palindrome. This approach achieves that without modifying the original strings.