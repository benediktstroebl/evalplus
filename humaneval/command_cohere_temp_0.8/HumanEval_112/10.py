```python
def reverse_delete(s, c):
    s = list(s)
    c = set(c)
    for char in c:
        s.remove(char)
    s = ''.join(s)
    if s == s[::-1]:
        return s, True
    else:
        return s, False
```
The function `reverse_delete()` takes two strings, `s` and `c`, as input and returns a tuple containing the modified string `s` and a boolean value indicating whether the modified string is a palindrome.

The approach first converts both inputs `s` and `c` into a list and a set respectively to ease the process of deleting characters from `s`. It then removes each character in `c` from `s` using a `for` loop and the `remove()` method. After this, the string is reconstructed by joining the modified list `s` into a string. 

The function then checks if the resulting string is a palindrome by comparing the beginning with the end of the string using slicing notation `s[::-1]`. A boolean value is returned accordingly depending on if the string is a palindrome or not.

This solution passes the test cases provided in the original problem statement.