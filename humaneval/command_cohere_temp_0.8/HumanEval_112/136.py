```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same value as s (initialise with empty string)
    
    for i, char in enumerate(s):
        if char not in delete:
            palindrome += char
    
    return palindrome, palindrome == palindrome[::-1]
```

The problem is solved using two main strings: `delete` and `palindrome`. The `delete` string contains characters from string `c` that need to be deleted. The `palindrome` string is initially set to an empty string and then sequentially appended with characters from string `s` if they are not in the `delete` string. After processing all characters, the second element of the returned tuple is established by comparing the `palindrome` string to its reverse using the `slicing` technique `palindrome[::-1]`. If the two are equal, the second return value is `True`, otherwise, it's `False`. 

This solution has a time complexity of `O(n + m)`, where `n` is the length of string `s` and `m` is the length of string `c`.