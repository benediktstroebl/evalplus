```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    if delete == delete[::-1]:
        return delete, True
    else:
        return delete, False
```
The algorithm for this solution involves:
- Removing all characters from `s` that are present in `c` (delete operation).
- Sorting the remaining characters in reverse order (`delete.reverse()`). This is to ensure that the characters are arranged in a way that preserves the palindrome property, even if the original string was reversed. 
- Appending an empty string to make the `delete` list a single string again.
- Checking if the resulting string is a palindrome. 

This solution leverages the fact that a string is a palindrome if and only if the reverse order of its characters is the same as the original order, to determine if the remaining characters form a palindrome. Importantly, the delete operation and the reverse operation are done sequentially, which makes the algorithm efficient. The code is also concise and easy to understand, making it an effective solution to the problem. P