```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reversed_s = s[:0]
    for i, char in enumerate(s):
        if char not in delete:
            reversed_s = reversed_s + char
    reversed_s = reversed(reversed_s)
    return (reversed_s, reversed_s == s)
```

This Python script provides a function called `reverse_delete`, which takes two strings as input and returns a tuple with the result of the deletion and a boolean indicating if the resulting string is a palindrome. 

The `delete` list stores the characters from the second string to delete from the first string. The `reversed_s` variable is initially initialized as an empty string and then iterates through the characters of the first string, adding any characters not in the `delete` list to the `reversed_s` variable. The reverse of `reversed_s` is then compared to the original string `s` to check if it is a palindrome and return the corresponding boolean value.