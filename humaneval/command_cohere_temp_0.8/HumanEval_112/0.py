```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The problem asks us to create a function `reverse_delete(s,c)` that takes two strings as input, `s` and `c`. This function must delete all characters in `s` that are present in `c`, i.e., character deletion. Then, we are asked to return the resulting string and a boolean indicating if it is a palindrome.

To solve this problem, we can use list comprehensions to delete characters in `s` that are in `c`, and use string concatenation to create the resulting string. We find the reverse of the resulting string and check if the original string is the same as its reverse to determine if it is a palindrome. We use boolean formatting to return a boolean value alongside the resulting string.

The code provided above adheres to the advertised specification, and any client code that relies on the advertised API of the function `reverse_delete(s,c)` will be duly satisfied.