```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    index = 0
    len_s = len(s)
    len_c = len(c)
    while index < len_s:
        if s[index] not in delete and reverse[index] not in delete:
            index += 1
        elif s[index] in delete and reverse[index] in delete:
            len_s -= 1
        else:
            index += 1
    if len_s <= 1:
        return s, False
    return s[:len_s], s[:len_s] == s[::-1]
```

The problem is solved in this Python script by using two strings `s` and `c`, where `s` is the string to be cleaned and checked for being a palindrome and `c` is a string of characters to be deleted. The script uses strings `delete` and `reverse` to store the characters from `c` and the reverse of `s` respectively, to easily index them for deletion. The script uses an index pointer to traverse the string `s` and remove characters that are found in `delete` and `reverse` simultaneously. Finally, the script returns the cleaned string `s` and a boolean indicating whether it's a palindrome or not. 

This solution has a time complexity of O(n), where n is the length of the input string `s`, due to the single traversal of the string `s` to identify and remove the characters specified in the delete string. The space complexity is O(1) since the function does not require any additional space.