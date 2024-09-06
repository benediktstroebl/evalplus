```python
def reverse_delete(s, c):
    s = ''.join(x for x in s if x not in c)
    return s, s == s[::-1]
```
The `reverse_delete()` function takes two strings as input, `s` and `c`. It uses a list comprehension to create a new string `s` that excludes any characters that are present in the string `c`. This way, it "deletes" from `s` all characters that are present in `c`. 

Then, the function returns a tuple containing the "deleted" string `s` and a boolean value indicating whether the remaining string is a palindrome. This is determined by checking whether the string `s` is equal to its reversed version `s[::-1]`.

This solution is efficient in terms of time and space complexity, as it only requires O(n) time to iterate over the strings and O(1) extra space for the list comprehension.