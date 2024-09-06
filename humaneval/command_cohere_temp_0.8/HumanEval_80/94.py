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

The script defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It first checks if the length of the string is at least 3; if not, it returns False. Then, it uses a set `letters_set` to store the letters encountered in the string. Every 3 consecutive letters must be distinct, so it checks if the set has reached a size of 3 or more and if the current letter is already present in the set; if so, it returns False. Finally, if the loop completes without encountering these conditions, the function returns True.