```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The `reverse_delete()` function takes two strings `s` and `c` as input and returns a tuple containing the modified string `s` and a boolean indicating whether the modified string is a palindrome. It first uses a list comprehension to create a new list with only the characters in `s` that are not in `c`, effectively deleting the characters in `s` that are present in `c`. Then, it joins this new list of characters back into a string to replace the original string `s`. Finally, it returns a tuple of this modified string and a boolean indicating whether the modified string is a palindrome, which is determined by checking if the string is equal to its reverse (`s == s[::-1]`). 

This approach ensures that the original strings `s` and `c` are not modified, and it efficiently deletes the characters in `s` that are equal to those in `c`. The result is a tuple containing the modified string and a boolean indicating whether the modified string is a palindrome. 

This code is self-contained and can be easily copied and run independently to test and verify its functionality. When necessary, it is adaptable and versatile enough to be readily expanded to account for more intricate situations or stricter border circumstances.