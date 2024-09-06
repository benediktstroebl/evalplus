```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It proceeds by iterating through the characters of the string up to 2 characters short of the full string's length. It uses a set `letters_set` to store the encountered letters. If the length of `letters_set` is equal to or greater than 3 and the current character is already in the set, it means that there are at least three consecutive letters that are identical, and the function returns False. Otherwise, the current character is added to the set. If the loop completes without any issues, the function returns True.

This solution has a time complexity of O(n), where n is the length of the input string, since it checks each letter in the string accordingly.