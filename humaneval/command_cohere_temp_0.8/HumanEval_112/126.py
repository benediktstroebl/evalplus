```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = [char for char in s if char not in delete and char in reverse]
    return result, result == result[::-1]
```

The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string `s` with all characters deleted that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. 

To solve the problem, the script uses two arrays:
- `delete` — Stores the characters from string `c` to be deleted from string `s`.
- `reverse` — The reversed version of string `s`. This is used to efficiently check whether the resulting string after deletion is a palindrome.

The `result` array is then filled with characters from `s` that are not in the `delete` array and are present in the `reverse` array. This step effectively deletes characters from `s` that are also in `c`.

The boolean value is then checked to determine if the resulting string is a palindrome by comparing it to its reverse. The final tuple is returned with the modified string and a boolean flag indicating whether it is a palindrome. 

This approach ensures that the characters in `c` are removed from `s`, and the palindrome aspect is efficiently checked using the reverse string.