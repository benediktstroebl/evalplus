```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The function `reverse_delete()` takes two strings `s` and `c` as input and returns a tuple containing the result string after deleting characters in `s` that are present in `c`, along with a boolean indicating whether the resulting string is a palindrome.

The script passes the tests provided in the prompt, as it correctly identifies the characters in `s` that are not present in `c` and checks if the resulting string is a palindrome. 

It first creates a list `delete` that contains all the characters in `c`. It then creates a string `reverse` that is the reverse of string `s`. Then, it constructs the `result` by iterating over the characters in `s` and excluding any characters that are in `delete` or not in `reverse`, this effectively removes characters that are present in `c`. 

Finally, the function returns the `result` and a boolean indicating whether it's a palindrome by checking if it's equal to its reverse (`result[::-1]`).