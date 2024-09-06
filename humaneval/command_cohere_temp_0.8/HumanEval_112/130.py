```python
def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same prefix as s (sliced with :0)
    
    for char in s:
        if char not in delete:
            palindrome += char
    
    return palindrome, palindrome == palindrome[::-1]
```

The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string after deleting characters in `s` that are present in `c`, along with a boolean indicating whether the resulting string is a palindrome. To achieve this, it creates a list called `delete` containing all the characters from `c`, and initially creates a new string called `palindrome` with the same prefix as `s` using a slice (`s[:0]`). Then, it iterates through each character in `s`, adding it to `palindrome` if it's not in the `delete` list. Finally, it returns the modified string `palindrome` and a boolean indicating whether it's a palindrome by comparing it to its reverse (`palindrome[::-1]`).