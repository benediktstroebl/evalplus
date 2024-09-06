```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reversed_s = s[:0]
    for char in s:
        if char not in delete:
            reversed_s = reversed_s + char
    return reversed_s, reversed_s == s
```

The function `reverse_delete()` takes two strings `s` and `c` as input and returns a tuple containing the result string after deleting characters in `s` that are present in `c`, and a boolean indicating whether the resulting string is a palindrome.

We start by creating an empty string `reversed_s` that will store the reversed version of the string `s`. We then use a list comprehension to create a list called `delete` which contains all the characters from string `c`. Next, we iterate through each character `char` in string `s` and check if the character is not in the `delete` list. If it is not, we append it to the `reversed_s` string. After processing all characters in `s`, we return a tuple containing the resulting string `reversed_s` and a boolean indicating whether it is a palindrome (i.e., whether it is equal to its reverse).

This approach has a time complexity of O(n), where n is the length of string `s`, due to the nested loop structure. The first loop iterates through each character in `s`, and the second loop iterates through each character in `c`.