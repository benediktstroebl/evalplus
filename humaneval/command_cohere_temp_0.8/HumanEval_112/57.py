```python
def reverse_delete(s, c):
    """Removes characters from s that are in c, then checks if the result is a palindrome."""
    s = [char for char in s if char not in c]
    return s, s == s[::-1]
```

This function leverages list comprehension to generate a new string s free from any characters also in the c string. It then checks whether the altered string is a palindrome by comparing it to its reverse using the slice s[::-1]. The function returns a tuple containing the palindrome-checked result and a boolean indicating whether the string is indeed a palindrome. 

This approach allows for an efficient and streamlined solution that upholds the palindrome check condition, all within a concise code footprint.