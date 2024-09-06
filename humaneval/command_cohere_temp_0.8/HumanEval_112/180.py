```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reversed_s = s[:0]
    for i, char in enumerate(s):
        if char not in delete:
            reversed_s = reversed_s + char
    return reversed_s, reversed_s == s
```

The function `reverse_delete()` takes two strings `s` and `c` as input and returns a tuple containing the result string after deleting characters in `s` that are present in `c`, and a boolean indicating whether the resulting string is a palindrome.

We start by creating an empty string `reversed_s` that will hold the reversed string after deleting the characters. The deletion is done by creating a list from `c` that holds the characters to be deleted. Then, we iterate through the characters of `s` using the `enumerate` function which gives the positions of the characters. We check if the current character is not in the list of characters to be deleted, and if so, we append it to `reversed_s`. The final result is a tuple containing `reversed_s` and a boolean indicating whether it is a palindrome by comparing it to the original string `s`.