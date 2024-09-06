```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] == s[i+1] and s[i] == s[i+2]:
            return False
        letters_set.add(s[i])
    return True
```

The function uses a set `letters_set` to store the letters of the given string `s`. It first checks if the length of the string is at least 3, and if so, it iterates over the string, checking if any 3 consecutive letters are identical. If they are, the function returns False. Otherwise, it returns True. 

You can test this function by calling it with different strings and verifying its correctness against the given test cases.